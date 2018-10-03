select b.client_id,mode,value_type,balance,allowed_credit,notify_client_balance,actual_notify_balance,
allowed_credit-percentage_notify_balance*allowed_credit/100 as bpt,last_lowbalance_time,
name,payment_term_id,company,billing_email,corporate_contact_email,
finance_email_cc,percentage_notify_balance,status,con.is_notify,c.is_daily_balance_notification,
duplicate_days,daily_send_time,send_time_type,last_alert_time,
(value_type=0 --value
   and  ((mode=1 and balance::numeric <= actual_notify_balance)
        or (mode=2 and balance::numeric <= notify_client_balance))
   ) as first,

(
  value_type=1
  and balance::numeric <= allowed_credit-percentage_notify_balance*allowed_credit/100
  ) as second
    from client c,c4_client_balance b,client_low_balance_config con where
c.client_id::text=b.client_id
and c.client_id=con.client_id
and c.is_daily_balance_notification and status
and
(
   (value_type=0 --value
   and  (
        (mode=1 and balance::numeric <= actual_notify_balance) or (mode=2 and balance::numeric <= notify_client_balance)
        )
   )
  or (
  value_type=1
  and balance::numeric <= allowed_credit-percentage_notify_balance*allowed_credit/100
  )
)
and
(   last_lowbalance_time is Null

  or(
    ( duplicate_days is NULL or extract(day from now() - last_lowbalance_time)  < duplicate_days )
    and
    ( extract(minute from  now()) >= 0 and extract(minute from  now()) < 5  )
    and
      (
      send_time_type = 0 and extract(hour from  now())::int = daily_send_time
      or send_time_type = 1
      )
     )
)


select c.client_id
    --,mode,value_type,balance,actual_notify_balance,notify_client_balance,allowed_credit-percentage_notify_balance*allowed_credit/100 as limit,last_lowbalance_time
    from client c,c4_client_balance b,client_low_balance_config con where
    c.client_id::text=b.client_id
    and c.client_id=con.client_id and status=true
    and not last_lowbalance_time is Null
    and (
       ( value_type=0
         and ((mode=1 and balance::numeric > actual_notify_balance) or
          (mode=2 and balance::numeric > notify_client_balance))
       )   or
       (
         value_type=1
         and balance::numeric > allowed_credit-percentage_notify_balance*allowed_credit/100 )
       )
