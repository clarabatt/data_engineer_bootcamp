# %%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import logging

# %%
url = 'https://vivareal.com.br/venda/bahia/salvador/apartamento_residencial/?pagina={}'

log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)


# %%
def get_apartments(page):
    rt = requests.get(url.format(i))
    return bs(rt.text)


i = 1
lst_apartments = []
lst_temp_apartments = get_apartments(i).find_all('a', {'class': 'property-card__content-link js-card-title'})
amount = float(get_apartments(i).find('strong', {'class': 'results-summary__count'}).text)

while len(lst_temp_apartments) > 0:
    print(i)
    lst_apartments = lst_apartments + lst_temp_apartments
    i += 1
    lst_temp_apartments = get_apartments(i)
    log.debug(f"Coletado {len(lst_apartments)} apartamentos da página {i}")

# %%
print(lst_apartments)
# apart = lst_temp_apartments[0]
# %%
df = pd.DataFrame(columns=['descrição', 'endereço', 'area', 'quartos', 'wc', 'vagas', 'valor', 'condominio', 'link'])

for apart in lst_apartments:
    try:
        descrição = apart.find('span', {'class': 'property-card__title'}).text.strip()
    except:
        descrição = None
    try:
        endereço = apart.find('span', {'class': 'property-card__address'}).text.strip()
    except:
        endereço = None
    try:
        area = apart.find('li', {'class': 'property-card__detail-area'}).text.strip()
    except:
        area = None
    try:
        quartos = apart.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
    except:
        quartos = None
    try:
        wc = apart.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
    except:
        wc = None
    try:
        vagas = apart.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
    except:
        vagas = None
    try:
        valor = apart.find('div', {'class': 'property-card__price'}).p.text.strip()
    except:
        valor = None
    try:
        condominio = apart.find('strong', {'class': 'js-condo-price'}).text.strip()
    except:
        condominio = None
    try:
        wlink = 'https://vivareal.com.br' + apart['href']
    except:
        wlink = None
    df.loc[df.shape[0]] = [descrição, endereço, area, quartos, wc, vagas, valor, condominio, wlink]

print(df)
# %%
