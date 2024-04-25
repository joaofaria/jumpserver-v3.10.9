# Instalação

1. **Atualize os pacotes do sistema:**

    ```bash
    sudo apt update
    ```

2. **Clone o repositório do JumpServer v3.10.9 para o diretório /opt/:**

    ```bash
    cd /opt/
    git clone https://github.com/joaofaria/jumpserver-v3.10.9.git
    cd jumpserver-v3.10.9
    ```

3. **Remova arquivos existentes e baixe os arquivos de GeoIP necessários:**

    ```bash
    rm -f apps/common/utils/ip/geoip/GeoLite2-City.mmdb apps/common/utils/ip/ipip/ipipfree.ipdb
    wget https://download.jumpserver.org/files/ip/GeoLite2-City.mmdb -O apps/common/utils/ip/geoip/GeoLite2-City.mmdb
    wget https://download.jumpserver.org/files/ip/ipipfree.ipdb -O apps/common/utils/ip/ipip/ipipfree.ipdb
    ```

## Bibliotecas

4. **Instale as bibliotecas necessárias:**

    ```bash
    apt-get install mysql-client libmysqlclient-dev
    apt-get install mysql-server
    apt install redis-tools redis-server
    apt-get install -y pkg-config libxmlsec1-dev libpq-dev libffi-dev libxml2 libxslt-dev libldap2-dev libsasl2-dev sshpass bash-completion g++ make sshpass
    ```

## Instalando Python

5. **Adicione o repositório DeadSnakes PPA e instale o Python 3.11:**

    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    apt-get install -y python3.11 python3.11-dev python3.11-venv
    python3.11 -m venv /opt/py3
    source /opt/py3/bin/activate
    ```

6. **Instale o Poetry para gerenciar as dependências do Python:**

    ```bash
    cd jumpserver-v3.10.9/
    pip install poetry==1.8.2
    ```

7. **Instale as dependências do projeto usando Poetry:**

    ```bash
    poetry install
    pip install mysqlclient
    ```

8. **Compile os arquivos de mensagens de localização:**

    ```bash
    rm -f apps/locale/zh/LC_MESSAGES/django.mo apps/locale/zh/LC_MESSAGES/djangojs.mo
    python apps/manage.py compilemessages
    ```

9. **Crie o usuario jumpserver no bd:**

    ```bash
    mysql -u root -p
    CREATE USER 'jumpserver'@'localhost' IDENTIFIED BY 'Wo6ri8je';
    GRANT ALL PRIVILEGES ON *.* TO 'novousuario'@'localhost';
    CREATE DATABASE jumpserver;
    FLUSH PRIVILEGES;
    EXIT;
    ```

## Iniciando o JumpServer

10. **Inicie o JumpServer no localhost:8080:**

    ```bash
    mkdir -p /opt/jumpserver-v3.10.9/tmp
    poetry run ./jms start
    ```

