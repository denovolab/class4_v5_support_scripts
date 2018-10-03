Python modules to be installed for python3:
psycopg2,  configparser,  requests , lockfile

subdir /logs  must be created before script execution
config.ini  is for postgress, debug level and http server address and port.

the server can be start with  ./dnl_import_dmon --action start
and can be stopped with: ./dnl_import_dmon --action stop
Use ./dnl_import_dmon --action debug for foreground debug output



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

debug_level = 1  - When activated more messages will be written in log files.





