#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
#%%
driver = webdriver.Chrome('./src/chromedriver')
driver.get('https://howedu.com.br')
# %%
driver.find_element(By.XPATH, '//*[@id="post-37"]/div/div/div/section[1]/div/div[1]/div/div[3]/div/div/a').click()
# %%
