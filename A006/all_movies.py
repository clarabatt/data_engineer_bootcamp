#%%
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

#%%
driver = webdriver.Chrome('./src/chromedriver')
time.sleep(5)
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
table_xpath = '//*[@id="mw-content-text"]/div[1]/table[2]'


#%%
def has_item(xpath: str, drv=driver):
    try:
        drv.find_element(By.XPATH, xpath)
        return True
    finally:
        return False


i = 0
while not has_item(table_xpath):
    i += 1
    if i > 50:
        break
    pass

#%%
table = driver.find_element(By.XPATH, table_xpath)

driver.close()

df = pd.read_html('<table>' + table.get_attribute('innerHTML') + '</table>')[0]


#%%
print(df[df['Ano'] == 1984])

#%%
df.to_csv('nicolas_cage_movies.csv', sep=';', index=False)
