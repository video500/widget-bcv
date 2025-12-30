cd ~/widget-bcv
curl -s -o bcv.html --cacert bcv-org-ve.pem https://www.bcv.org.ve
curl -s -o telegram_dolar.html https://t.me/s/MonitorDolarVeOFICIAL
python widget-bcv.py | termux-notification -t "Dólar hoy"


