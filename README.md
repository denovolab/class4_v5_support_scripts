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

