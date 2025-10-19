Kognitivni Agent 1 - Micko 
--------------------------

Instalacija:

Konfigurirati Apache poslužitelj:

SSLCertificateFile /etc/letsencrypt/live/dragon.foi.hr-0001/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/dragon.foi.hr-0001/privkey.pem
Include /etc/letsencrypt/options-ssl-apache.conf

WSGIDaemonProcess jura user=www-data group=www-data threads=5
WSGIScriptAlias /jura /home/markus/agenti-fsa/server/jura.wsgi

<Directory /home/markus/agenti-fsa/server>
    WSGIProcessGroup jura
    WSGIApplicationGroup %{GLOBAL}
    Require all granted
</Directory>

SSLProxyEngine On
ProxyRequests Off

<Location /ws/>
        ProxyPass wss://localhost:8009/
        ProxyPassReverse wss://localhost:8009/
    </Location>

U datoteci: /etc/apache2/sites-available/dragon.foi.hr-le-ssl.conf

Aktivirati apache2 module

sudo a2enmod headers
sudo a2enmod proxy
sudo a2enmod proxy_wstunnel
sudo a2enmod proxy_http

Uspostaviti wss servis:

U mapu: /etc/systemd/system/ staviti datoteku fsa-jura.service

Aktivirati servis sa:

sudo systemctl enable fsa-jura
sudo systemctl start fsa-jura
