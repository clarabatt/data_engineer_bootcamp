#%%
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

#%%
driver = webdriver.Chrome('./src/chromedriver')
time.sleep(5)
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
table = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]')
driver.close()

#%%
df = pd.read_html('<table>' + table.get_attribute('innerHTML') + '</table>')[0]

#%%
df[df['Ano']==1984]

#%%
df.to_csv('nicolas_cage_movies.csv', sep=';', index=False)
