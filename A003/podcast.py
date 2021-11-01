#%%
import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd
#%%
url = "https://portalcafebrasil.com.br/todos/podcasts/"
req = requests.get(url)
podcasts = bs(req.text)
#%%
podcasts.find('h5')
#%%
podcasts.find('h5').text
#%%
podcasts.find('h5').a['href']
#%%
lst_podcasts = podcasts.find_all('h5')

for item in lst_podcasts:
    print(f"Episódio: {item.text} - Link: {item.a['href']}")

#%%
url = "https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true"
url.format(5)

#%%
def get_podcasts(new_url):
    req = requests.get(new_url)
    soup = bs(req.text)
    return soup.find_all('h5')

#%%
get_podcasts(url.format(5))
#%%

log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

i = 1
lst_podcasts = []
lst_temp = get_podcasts(url.format(i))
log.debug(f"Coletado {len(lst_temp)} episódios do link {url.format(i)}")

while len(lst_temp) > 0:
    lst_podcasts = lst_podcasts + lst_temp
    i += 1
    lst_temp = get_podcasts(url.format(i))
    log.debug(f"Coletado {len(lst_temp)} episódios do link {url.format(i)}")

#%%
lst_podcasts
#%%
len(lst_podcasts)
#%%
df = pd.DataFrame(columns=['name', 'link'])
for item in lst_podcasts:
    df.loc[df.shape[0]] = [item.text, item.a['href']]

df.shape

#%%
df
#%%
df.to_csv('banco_de_podcasts.csv', sep=';', index=False)