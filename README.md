Denovolab v5 support scripts, this a collection of utilities that make web ui create statistic,billing, invoices, generate alerts and monitor traffic.
Supported OS is Centos 7
Scripts are written in python 3.5.

requirements for this:

install python3.5
after that install these modules:
psycopg2
configparser
flask
Flask-WTF
requests
pillow
reportlab
python-dateutil
lockfile
phpserialize
xlrd 
pytz 
psutil
aiohttp==1.3.4
aiopg==0.13.0
async-timeout==1.2.1
chardet==3.0.2
multidict==2.1.4
olefile==0.44
Pillow==4.1.1
psycopg2==2.7.1
reportlab==3.4.0
requests==2.13.0
SQLAlchemy==1.1.9
yarl==0.9.8
asn1crypto==0.22.0
bcrypt==3.1.3
cachetools==2.0.1
certifi==2015.4.28
cffi==1.10.0
chardet==3.0.4
click==6.7
cryptography==2.0.3
docutils==0.14
Flask==0.12.2
google-auth==1.0.2
google-cloud-core==0.26.0
google-cloud-storage==1.3.2
google-resumable-media==0.2.3
googleapis-common-protos==1.5.2
idna==2.6
itsdangerous==0.24
Jinja2==2.9.6
lockfile==0.12.2
MarkupSafe==1.0
monotonic==1.3
paramiko==2.2.1
protobuf==3.4.0
psycopg2==2.7.3
pyasn1==0.3.2
pyasn1-modules==0.0.11
pycparser==2.18
pycrypto==2.6.1
PyNaCl==1.1.2
python-daemon==2.1.2
requests==2.18.4
rsa==3.4.2
six==1.10.0
tenacity==4.4.0
urllib3==1.22
Werkzeug==0.12.2

for pcap2, you would need to patch python daemon, just copy and overwrite files from thirdparty folder into your python instalation /site packages dir.
every folder has ini file which can be used to modify configuration if needed.  in the provided systemd service files are one way of running these scripts.
in order to succesfully start these scripts, database must be installed, and programs for engine started first.

default instalaltion path is /opt/denovo/
so it would look like this:

/opt/denovo/dnl_alerts 
/opt/denovo/dnl_data_import  
/opt/denovo/dnl_did_billing  
/opt/denovo/dnl_invoice_generator  
/opt/denovo/dnl_monitoring  
/opt/denovo/dnl_rt_index  
/opt/denovo/dnl_web_helper...

For the pcap2 script, copy files from thirdparty into /python_lib_path/python3.5/site_packages (overwrite files there)
also copy file from /etc folder into /etc/sudoers.d
for this script you also need to configure ip youre using for sip, so it will caputure packets 
default storage is set to local, but it can also be configured to use ftp, or google bucket.

copy systemd files into /etc/systemd/system

run each script as service wiht systwemctl
eg.
systemctl start dnl_alerts, systemctl start dnl_data_import....
to enable scripts at startup  do a systemctl enable dnl_alerts, systemctl enable dnl_data_import .....

before using this scripts, make sure that database has been installed.
if any of the scripts failed to start, it will not affect working of the engine, but it can affect data showing in the ui, generating reports, and etc...
