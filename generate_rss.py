import requests
from bs4 import BeautifulSoup

# Lista de URLs a rastrear
urls = [
    "https://lamenteesmaravillosa.com/neurociencias/",
    "https://lamenteesmaravillosa.com/trabajo/",
    "https://psicologiaymente.com/categoria/drogas",
    "https://psicologiaymente.com/categoria/personalidad",
    "https://psicologiaymente.com/categoria/organizaciones",
    "https://psicologiaymente.com/categoria/neurociencias",
    "https://psicologiaymente.com/categoria/forense",
    "https://psicologiaymente.com/categoria/desarrollo",
    "https://psicologiaymente.com/categoria/psicofarmacologia",
    "https://psicologiaymente.com/categoria/consumidor",
    "https://psicologiaymente.com/categoria/inteligencia",
    "https://psicologiaymente.com/tags/historia-de-la-psicologia",
    "https://psicologiaymente.com/tags/narcisismo",
    "https://psicologiaymente.com/tags/teoria",
    "https://psicologiaymente.com/tags/depresion",
    "https://psicologiaymente.com/marketing",
    "https://www.psicologia-online.com/pir/",
    "https://psicologiaymente.com/tags/terapia",
    "https://psicologiaymente.com/tags/emocion"
]

titulares = []

for url in urls:
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        
        # Extrae títulos: h1, h2 y h3 (ajustable)
        for tag in ["h1", "h2", "h3"]:
            for element in soup.find_all(tag):
                text = element.get_text(strip=True)
                if text and text not in titulares:  # evitar duplicados
                    titulares.append(text)
    except Exception as e:
        print(f"No se pudo procesar {url}: {e}")

# Mostrar resultados (para pruebas)
for t in titulares:
    print(t)
