#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#%%
driver = webdriver.Chrome('./src/chromedriver')
driver.get('https://howedu.com.br')

# %%
driver.find_element(By.XPATH, '//*[@id="post-37"]/div/div/div/section[1]/div/div[1]/div/div[3]/div/div/a').click()

# %%
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
elem_cep = driver.find_element(By.NAME, 'endereco')

# %%
elem_cep.clear()
elem_cep.send_keys('41940040')

# %%
elem_type = Select(driver.find_element(By.NAME, 'tipoCEP'))

# %%
elem_type.select_by_value('LOG')

# %%
driver.find_element(By.ID, 'btn_pesquisar').click()