##Instalação
sudo apt update

cd /opt/
git clone https://github.com/joaofaria/jumpserver-v3.10.9.git
cd jumpserver-v3.10.9
rm -f apps/common/utils/ip/geoip/GeoLite2-City.mmdb apps/common/utils/ip/ipip/ipipfree.ipdb
wget https://download.jumpserver.org/files/ip/GeoLite2-City.mmdb -O apps/common/utils/ip/geoip/GeoLite2-City.mmdb
wget https://download.jumpserver.org/files/ip/ipipfree.ipdb -O apps/common/utils/ip/ipip/ipipfree.ipdb

##Bibliotecas
apt-get install -y pkg-config libxmlsec1-dev libpq-dev libffi-dev libxml2 libxslt-dev libldap2-dev libsasl2-dev sshpass bash-completion g++ make sshpass
apt-get install -y libmariadb-dev

##Instalando Python
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
apt-get install -y python3.11 python3.11-dev python3.11-venv
python3.11 -m venv /opt/py3
source /opt/py3/bin/activate
sudo apt-get install

#Instalando Poetry
pip install poetry==1.8.2

#Instalando Dependências
poetry install

rm -f apps/locale/zh/LC_MESSAGES/django.mo apps/locale/zh/LC_MESSAGES/djangojs.mo
python apps/manage.py compilemessages

#Iniciando no localhost:8080
poetry run ./jms start
