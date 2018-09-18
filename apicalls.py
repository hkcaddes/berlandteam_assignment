# call ingredient API

# import libraries
import requests
import pandas as pd
import json

17/1735*100

# base url for api product/ingredient search
base_url = 'https://skincare-api.herokuapp.com/product?q='
base_url2 = 'https://skincare-api.herokuapp.com/products'


response2 = requests.get(base_url2)
data2 = response2.json()
len(data2)


# Niacinamide
response = requests.get(base_url + 'niacinamide')
data = response.json()
len(data)

# Heparan Sulfate
response = requests.get(base_url + "seed")
data = response.json()
len(data)/1735
data
