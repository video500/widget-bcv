from bs4 import BeautifulSoup
import requests

#url="https://www.bcv.org.ve/"
url_bcv="bcv.html"
url_telegram="telegram_dolar.html"

def load_html(url):
#response = requests.get(url, verify="bcv-org-ve-chain.pem")
    with open(url,"r", encoding="utf-8") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")

soup= load_html(url_bcv)
soup_telegram= load_html(url_telegram)

# Extraer información de un div con clase específica
dolar_div = soup.find("div", id="dolar")
if dolar_div:
    valor = dolar_div.find("div", class_="centrado").strong.text.strip()  # Extrae el texto dentro de <strong>
else:
    valor = "Error"

euro_div = soup.find("div", id="euro")
if euro_div:
    valore = euro_div.find("div", class_="centrado").strong.text.strip()  # Extrae el texto dentro de <strong>
else:
    valore = "Error"
    
fecha_span = soup.find("span", class_="date-display-single")

if fecha_span:
    fecha_texto = fecha_span.text.strip()  # Extrae el texto visible (ej. Miércoles, 23 Abril 2025)
    fecha_iso = fecha_span["content"]  # Extrae la fecha en formato ISO (ej. 2025-04-23T00:00:00-04:00)
else:
    fecha_texto = "Error Fecha"

# Procesar Telegram channel

divs = soup_telegram.find_all("div", class_="tgme_widget_message_text js-message_text")

# Filtrar los divs que contienen el emoji 🕒
divs_con_emoji = [div for div in divs if "🕒" in div.get_text()]

# Seleccionar el último de la lista filtrada
ultimo_div = divs_con_emoji[-1] if divs_con_emoji else None

# Mostrar el contenido del último div si existe
textos_paralelo="Indefinido"
if ultimo_div:
    textos_paralelo = ultimo_div.get_text()#.split("\n")
#    datos = {
#        "fecha": textos.split("🗓")[-1].strip(),
#        "hora": textos.split("🕒")[-1].strip(),
#        "valor": textos.split("💵")[-1].strip(),
#        "variacion": textos.split("🔻")[-1].strip(),
#        "brecha": textos.split("↔️")[-1].strip()
#    }
#    print(datos)
else:
    print("No se encontraron elementos que coincidan.")
    
print (f"{fecha_texto}\nDolar: {valor}\nEuro: {valore}\nParalelo\n{textos_paralelo}")

