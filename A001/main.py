import requests
import pandas as pd
import collections

url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0sTIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAcySpRM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/'

r = requests.get(url)
r_text = r.text
df = pd.read_html(r_text)

# type(df)
# type(df[0])

df = df[0].copy()
nr_pop = list(range(1, 26))
nr_pares = list(range(2, 25, 2))
nr_impares = list(range(1, 26, 2))
nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]

comb = []
v_numbers = {
    'v_1': 0,
    'v_2': 0,
    'v_3': 0,
    'v_4': 0,
    'v_5': 0,
    'v_6': 0,
    'v_7': 0,
    'v_8': 0,
    'v_9': 0,
    'v_10': 0,
    'v_11': 0,
    'v_12': 0,
    'v_13': 0,
    'v_14': 0,
    'v_15': 0,
    'v_16': 0,
    'v_17': 0,
    'v_18': 0,
    'v_19': 0,
    'v_20': 0,
    'v_21': 0,
    'v_22': 0,
    'v_23': 0,
    'v_24': 0,
    'v_25': 0
}

lst_campos = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']

for index, row in df.iterrows():
    V_PARES = 0
    V_IMPARES = 0
    V_PRIMOS = 0
    for campo in lst_campos:
        if row[campo] in nr_pares:
            V_PARES += 1
        if row[campo] in nr_impares:
            V_IMPARES += 1
        if row[campo] in nr_primos:
            V_PRIMOS += 1
        for n in nr_pop:
            if row[campo] == n:
                v_numbers["v_{}".format(n)] += 1

    comb.append(str(V_PARES) + 'p-' + str(V_IMPARES) + 'i-' + str(V_PRIMOS) + 'np')

less_fr = min(v_numbers, key=v_numbers.get)
high_fr = max(v_numbers, key=v_numbers.get)

counter = collections.Counter(comb)
result = pd.DataFrame(counter.items(), columns=['combinação', 'frequencia'])
result['p_freq'] = result['frequencia']/result['frequencia'].sum()
result = result.sort_values(by='p_freq')