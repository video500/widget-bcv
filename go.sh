cd ~/widget-bcv
curl -o bcv.html --cacert bcv-org-ve.pem https://www.bcv.org.ve
curl -o telegram_dolar.html https://t.me/s/monitornoticiasvzla
python widget-bcv.py | termux-notification -t "Dólar hoy"


