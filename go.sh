cd ~/widget-bcv
curl -o bcv.html --cacert bcv-org-ve.pem https://www.bcv.org.ve
python widget-bcv.py | termux-notification -t "Dólar hoy"


