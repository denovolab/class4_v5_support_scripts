Python modules to be installed for python3:
psycopg2,  configparser, flask , Flask-WTF , requests ,python-dateutil

Check subfolders for existence  /app/invoice and /logs.
config.ini  is for postgress, debug level and http server address and port.


The API has two parts:
Autoinvoice: AutoInvoice.py.
REST API: RunFlask.py 

Host and port must be set in config.ini





Logging: It is using  TimedRotatingFileHandler or RotatingFileHandler which must be set from config.ini[log][by_time]. When is = 1, then is by time. otherwise is by size. File path must exist!
alert_rules_when  option. They are not case sensetive: 
'S'	Seconds
'M'	Minutes
'H'	Hours
'D'	Days
'W0'-'W6'	Weekday (0=Monday)
'midnight'	Roll over at midnight

When using weekday-based rotation, specify ‘W0’ for Monday, ‘W1’ for Tuesday, and so on up to ‘W6’ for Sunday. In this case, the value passed for interval isn’t used.
The system will save old log files by appending extensions to the filename. The extensions are date-and-time based, using the strftime format %Y-%m-%d_%H-%M-%S or a leading portion thereof, depending on the rollover interval.

For handling by size:
When backupCount is non-zero, the system will save old log files by appending the extensions ‘.1’, ‘.2’ etc., to the filename. For example, with a backupCount of 5 and a base file name of app.log, you would get app.log, app.log.1, app.log.2, up to app.log.5

configuration file :  config.ini
[other] [logo_file_get]  - is the URL of UI get logo request. It is the address of UI + /homes/getInvoiceLogoUrl - for example if the UI is at the address http://http://192.99.10.113
then this URL must be set to: http://192.99.10.113/homes/getInvoiceLogoUrl


debug_level = 1  - When activated more messages will be written in log files.


./RunFlask.py   - this is a web server for surving pdf invoice files and getting POST requests from UI
./app/  - the server is using flask-python  framework. App subfolder is used primary by the framework.
./app/invoice - here are stored invoice pdf files and there logs
./AutoInvoice.py -main Auto invoice logic
./manualinvoice.py  - main Manual Invoice logic
./config.ini - settings
./logo.jpg - local file for storing switch logo. The script will download fresh logo from server when pdf must be created  , resize the logo and store it here
./blank_logo - if server logo is missing the script will use this
./logs

Version from 21-01-2018



REST API:
It must be used POST request to http://host:port/ManualInvoiceTest

Complete request looks this way (all options are used ,when an option is not used, it must be omitted from POST request)
 ImmutableMultiDict([('show_trafic_country', 'on'), ('invoice_use_balance_type', '0'), ('fields', 'Array'), ('_method', 'POST'), ('query', 'Array'), ('detail_by_trunk', 'on'), ('type', '0'), ('dayusage', 'on'), ('client_id', '3'),
 ('end_date', '2018-01-21 23:59:59'), ('start_time', '00:00:00'), ('is_invoice_account_summary', 'on'), ('decimal_place', '5'), ('start_date', '2018-01-15 00:00:00'), ('void_id', ''), ('is_short_duration_call_surcharge_detail', 'on'),
 ('stop_time', '23:59:59'), ('ingress_prefix', 'on'), ('show_trafic_code_name', 'on'), ('summary_of_payments', 'on'), ('show_calls_date', 'on'), ('invoice_date', '2018-01-25'), ('show_account_summary', 'on'), ('invoice_due_date', '2018-01-25'),
 ('is_invoice_usage_detail', 'on')])


