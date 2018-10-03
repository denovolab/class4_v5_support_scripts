 
    
select  t.client_id , t.description,
   CASE 
     WHEN date_trunc('month', coalesce(did_fees_history.did_fixed_fees_last_payment, CURRENT_DATE - INTERVAL '1 months')) < 
        date_trunc('month', '2018-01-24'::date) THEN t.fee
     else 0.0
   END AS fee  ,
   date_trunc('month', coalesce(did_fees_history.did_fixed_fees_last_payment, CURRENT_DATE - INTERVAL '1 months')) as last_paid_fees 
   ,client.mode FROM client
    INNER JOIN
     (    SELECT t.client_id,t.description, t.fee
    FROM (
        SELECT    resource.client_id ,'One-time Setup Fee for DID ' || did_billing_rel.did AS description,
            CASE 
                WHEN date_trunc('month', coalesce(did_billing_rel.start_date, CURRENT_DATE)) = 
                    date_trunc('month', '2018-01-24'::date) THEN coalesce(did_billing_plan.did_price, 0.0)
                ELSE 0.0
            END AS fee
        FROM resource
            INNER JOIN did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.sell_billing_plan_id = did_billing_plan.id
        WHERE resource.egress 
        UNION ALL
        SELECT resource.client_id, 'Monthly Fee for DID ' || did_billing_rel.did AS description, 
            did_billing_rel.days / did_billing_rel.days_in_month * coalesce(did_billing_plan.monthly_charge, 0.0) AS fee
        FROM resource
            INNER JOIN (
                SELECT t.did, t.ingress_res_id, t.sell_billing_plan_id, t.days_in_month, t.end_date - t.start_date + 1 AS days
                FROM (
                    SELECT did_billing_rel.did, did_billing_rel.ingress_res_id, did_billing_rel.sell_billing_plan_id,
                        date_part('days', date_trunc('month', '2018-01-24'::date) + '1 MONTH'::interval - '1 DAY'::interval) AS days_in_month,
                        GREATEST(did_billing_rel.start_date, date_trunc('month', '2018-01-24'::date)::date) AS start_date,
                        LEAST(did_billing_rel.end_date, date_trunc('month', '2018-01-24'::date) + '1 MONTH'::interval - '1 DAY'::interval)::date AS end_date
                    FROM did_billing_rel
                ) t
                WHERE t.end_date - t.start_date > -1) did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.sell_billing_plan_id = did_billing_plan.id
        WHERE resource.egress 
            AND did_billing_rel.days / did_billing_rel.days_in_month * coalesce(did_billing_plan.monthly_charge, 0.0) > 0
    ) AS t
    WHERE t.fee > 0
    UNION ALL  
    
   SELECT resource.client_id , 'Port Fee for DID ' || did_billing_rel.did AS description,  resource.dnis_cap_limit* did_billing_rel.fee_per_port as fee 
        FROM resource
            INNER JOIN (
                SELECT t.did,  t.buy_billing_plan_id, t.days_in_month, t.end_date - t.start_date + 1 AS days, t.fee_per_port as fee_per_port, t.egress_res_id,
                t.ingress_res_id
                 FROM (
                    SELECT did_billing_rel.did,  did_billing_rel.ingress_res_id,did_billing_rel.egress_res_id,did_billing_rel.buy_billing_plan_id,did_billing_rel.fee_per_port,
                        date_part('days', date_trunc('month', '2018-01-24'::date) + '1 MONTH'::interval - '1 DAY'::interval) AS days_in_month,
                        GREATEST(did_billing_rel.start_date, date_trunc('month', '2018-01-24'::date)::date) AS start_date,
                        LEAST(did_billing_rel.end_date, date_trunc('month', '2018-01-24'::date) + '1 MONTH'::interval - '1 DAY'::interval)::date AS end_date
                    FROM did_billing_rel
                ) t
                WHERE t.end_date - t.start_date > -1) did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.buy_billing_plan_id = did_billing_plan.id
        WHERE resource.egress 
            AND did_billing_rel.days / did_billing_rel.days_in_month * (  coalesce(did_billing_rel.fee_per_port, 0.0)* coalesce(resource.dnis_cap_limit, 0.0) ) > 0      
    
     ) as t  on client.client_id = t.client_id 
    LEFT JOIN
         did_fees_history on did_fees_history.client_id = t.client_id  ;
          
   
  fee_per_port
  
  
  
   SELECT 'Port Fee for DID ' || did_billing_rel.did AS description, 
            coalesce(did_billing_rel.fee_per_port ) AS fee_per_port, resource.dnis_cap_limit , resource.dnis_cap_limit* did_billing_rel.fee_per_port as port_fee_total
        FROM resource
            INNER JOIN (
                SELECT t.did,  t.buy_billing_plan_id, t.days_in_month, t.end_date - t.start_date + 1 AS days, t.fee_per_port as fee_per_port, t.egress_res_id,
                t.ingress_res_id
                 FROM (
                    SELECT did_billing_rel.did,  did_billing_rel.ingress_res_id,did_billing_rel.egress_res_id,did_billing_rel.buy_billing_plan_id,did_billing_rel.fee_per_port,
                        date_part('days', date_trunc('month', '2018-01-24'::date) + '1 MONTH'::interval - '1 DAY'::interval) AS days_in_month,
                        GREATEST(did_billing_rel.start_date, date_trunc('month', '2018-01-24'::date)::date) AS start_date,
                        LEAST(did_billing_rel.end_date, date_trunc('month', '2018-01-24'::date) + '1 MONTH'::interval - '1 DAY'::interval)::date AS end_date
                    FROM did_billing_rel
                ) t
                WHERE t.end_date - t.start_date > -1) did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.buy_billing_plan_id = did_billing_plan.id
        WHERE resource.egress 
            AND did_billing_rel.days / did_billing_rel.days_in_month * (  coalesce(did_billing_rel.fee_per_port, 0.0)* coalesce(resource.dnis_cap_limit, 0.0) ) > 0  ;
            
            
            
        ---------------------    
            WEEKLY
        --------------------
            
            
            
            
            
            select  t.client_id , t.description,t.fee as fee  ,
   did_fees_history.did_fixed_fees_last_payment::date as last_paid_fees  
   ,did_fees_history.port_fee_last_payment::date  as port_fee_last_payment , did_fees_history.one_time_setup_fee_paid as one_time_setup_fee_paid
   ,client.mode ,  t.pay_type  FROM client
    INNER JOIN
     (    SELECT t.client_id,t.description, t.fee ,t.pay_type
    FROM (
        SELECT    resource.client_id ,'One-time Setup Fee for DID ' || did_billing_rel.did AS description,
            CASE 
                WHEN date_trunc('month', coalesce(did_billing_rel.start_date, CURRENT_DATE)) = 
                    date_trunc('month', '2018-02-01'::date) THEN coalesce(did_billing_plan.did_price, 0.0)
                ELSE 0.0
            END AS fee , did_billing_plan.pay_type as pay_type
        FROM resource
            INNER JOIN did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.sell_billing_plan_id = did_billing_plan.id
        WHERE resource.egress 
        
        UNION ALL
        
        SELECT resource.client_id, 'Season Fee for DID ' || did_billing_rel.did AS description, 
            did_billing_rel.days / did_billing_rel.days_in_month * coalesce(did_billing_plan.monthly_charge, 0.0) AS fee , did_billing_plan.pay_type as pay_type
        FROM resource
            INNER JOIN (
                SELECT t.did, t.ingress_res_id, t.sell_billing_plan_id, t.days_in_month, t.end_date - t.start_date + 1 AS days, t.start_date,t.end_date
                FROM (
                    SELECT did_billing_rel.did, did_billing_rel.ingress_res_id, did_billing_rel.sell_billing_plan_id,
                        date_part('days', date_trunc('month', '2018-02-01'::date) + '1 MONTH'::interval - '1 DAY'::interval) AS days_in_month,
                        GREATEST(did_billing_rel.start_date, '2018-02-01'::date  - '7 DAY'::interval  -'1 SECOND'::interval  )::date AS start_date,
                        LEAST(did_billing_rel.end_date, '2018-02-01'::date -'1 SECOND'::interval   )::date AS end_date
                    FROM did_billing_rel
                ) t
                WHERE t.end_date - t.start_date > -1) did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.sell_billing_plan_id = did_billing_plan.id
        WHERE resource.egress  AND did_billing_plan.pay_type = 0 
            AND did_billing_rel.days / did_billing_rel.days_in_month * coalesce(did_billing_plan.monthly_charge, 0.0) > 0
    ) AS t
    WHERE t.fee > 0
    
    UNION ALL  
    
   SELECT resource.client_id , 'Port Fee for DID ' || did_billing_rel.did AS description,  resource.dnis_cap_limit* did_billing_rel.fee_per_port as fee , did_billing_plan.pay_type as pay_type
        FROM resource
            INNER JOIN (
                SELECT t.did,  t.buy_billing_plan_id, t.days_in_month, t.end_date - t.start_date + 1 AS days, t.fee_per_port as fee_per_port, t.egress_res_id,
                t.ingress_res_id
                 FROM (
                    SELECT did_billing_rel.did,  did_billing_rel.ingress_res_id,did_billing_rel.egress_res_id,did_billing_rel.buy_billing_plan_id,did_billing_rel.fee_per_port,
                        date_part('days', date_trunc('month', '2018-02-01'::date) + '1 MONTH'::interval - '1 DAY'::interval) AS days_in_month,
                        GREATEST(did_billing_rel.start_date, date_trunc('month', '2018-02-01'::date)::date) AS start_date,
                        LEAST(did_billing_rel.end_date, date_trunc('month', '2018-02-01'::date) + '1 MONTH'::interval - '1 DAY'::interval)::date AS end_date
                    FROM did_billing_rel
                ) t
                WHERE t.end_date - t.start_date > -1) did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.buy_billing_plan_id = did_billing_plan.id
        WHERE resource.egress 
            AND did_billing_rel.days / did_billing_rel.days_in_month * (  coalesce(did_billing_rel.fee_per_port, 0.0)* coalesce(resource.dnis_cap_limit, 0.0) ) > 0      
    
     ) as t  on client.client_id = t.client_id 
    LEFT JOIN
         did_fees_history on did_fees_history.client_id = t.client_id  
            
            
            
            
            
            
            
            
                        
        ---------------------    
            MONTHLY
        --------------------
            
            
            
            
                     
            
            select  t.client_id , t.description,
   CASE 
     WHEN date_trunc('month', coalesce(did_fees_history.did_fixed_fees_last_payment, CURRENT_DATE - INTERVAL '1 months')) < 
        date_trunc('month', '2018-01-29'::date) THEN t.fee
     else 0.0
   END AS fee  ,
   date_trunc('month', coalesce(did_fees_history.did_fixed_fees_last_payment, CURRENT_DATE - INTERVAL '1 months')) as last_paid_fees  
   ,client.mode ,  t.pay_type  FROM client
    INNER JOIN
     (    SELECT t.client_id,t.description, t.fee ,t.pay_type
    FROM (
        SELECT    resource.client_id ,'One-time Setup Fee for DID ' || did_billing_rel.did AS description,
            CASE 
                WHEN date_trunc('month', coalesce(did_billing_rel.start_date, CURRENT_DATE)) = 
                    date_trunc('month', '2018-01-29'::date) THEN coalesce(did_billing_plan.did_price, 0.0)
                ELSE 0.0
            END AS fee , did_billing_plan.pay_type as pay_type
        FROM resource
            INNER JOIN did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.sell_billing_plan_id = did_billing_plan.id
        WHERE resource.egress 
        
        UNION ALL
        
        SELECT resource.client_id, 'Season Fee for DID ' || did_billing_rel.did AS description, 
            did_billing_rel.days / did_billing_rel.days_in_month * coalesce(did_billing_plan.monthly_charge, 0.0) AS fee , did_billing_plan.pay_type as pay_type
        FROM resource
            INNER JOIN (
                SELECT t.did, t.ingress_res_id, t.sell_billing_plan_id, t.days_in_month, t.end_date - t.start_date + 1 AS days
                FROM (
                    SELECT did_billing_rel.did, did_billing_rel.ingress_res_id, did_billing_rel.sell_billing_plan_id,
                        date_part('days', date_trunc('month', '2018-01-29'::date) + '1 MONTH'::interval - '1 DAY'::interval) AS days_in_month,
                        GREATEST(did_billing_rel.start_date, date_trunc('month', '2018-01-29'::date)::date) AS start_date,
                        LEAST(did_billing_rel.end_date, date_trunc('month', '2018-01-29'::date) + '1 MONTH'::interval - '1 DAY'::interval)::date AS end_date
                    FROM did_billing_rel
                ) t
                WHERE t.end_date - t.start_date > -1) did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.sell_billing_plan_id = did_billing_plan.id
        WHERE resource.egress  AND did_billing_plan.pay_type = 0 
            AND did_billing_rel.days / did_billing_rel.days_in_month * coalesce(did_billing_plan.monthly_charge, 0.0) > 0
    ) AS t
    WHERE t.fee > 0
    
    UNION ALL  
    
   SELECT resource.client_id , 'Port Fee for DID ' || did_billing_rel.did AS description,  resource.dnis_cap_limit* did_billing_rel.fee_per_port as fee , did_billing_plan.pay_type as pay_type
        FROM resource
            INNER JOIN (
                SELECT t.did,  t.buy_billing_plan_id, t.days_in_month, t.end_date - t.start_date + 1 AS days, t.fee_per_port as fee_per_port, t.egress_res_id,
                t.ingress_res_id
                 FROM (
                    SELECT did_billing_rel.did,  did_billing_rel.ingress_res_id,did_billing_rel.egress_res_id,did_billing_rel.buy_billing_plan_id,did_billing_rel.fee_per_port,
                        date_part('days', date_trunc('month', '2018-01-29'::date) + '1 MONTH'::interval - '1 DAY'::interval) AS days_in_month,
                        GREATEST(did_billing_rel.start_date, date_trunc('month', '2018-01-29'::date)::date) AS start_date,
                        LEAST(did_billing_rel.end_date, date_trunc('month', '2018-01-29'::date) + '1 MONTH'::interval - '1 DAY'::interval)::date AS end_date
                    FROM did_billing_rel
                ) t
                WHERE t.end_date - t.start_date > -1) did_billing_rel ON did_billing_rel.ingress_res_id = resource.resource_id
            INNER JOIN did_billing_plan ON did_billing_rel.buy_billing_plan_id = did_billing_plan.id
        WHERE resource.egress 
            AND did_billing_rel.days / did_billing_rel.days_in_month * (  coalesce(did_billing_rel.fee_per_port, 0.0)* coalesce(resource.dnis_cap_limit, 0.0) ) > 0      
    
     ) as t  on client.client_id = t.client_id 
    LEFT JOIN
         did_fees_history on did_fees_history.client_id = t.client_id     
            
            

            
            
