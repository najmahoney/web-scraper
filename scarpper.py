from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/search?q=Fujifilm+X-T30&rlz=1C5CHFA_enUS1049US1049&oq=Fujifilm+X-T30&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIQCAEQLhiDARixAxiABBjlBDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIGCAcQRRg80gEHMjA1ajBqNKgCALACAA&sourceid=chrome&ie=UTF-8'

response = requests.get(url)
doc = BeautifulSoup(response.text, 'html.parser')

prices = doc.find_all(text='$')

parent_prices = prices[0].parent_prices
strong = parent_prices.find('strong')
print(strong.string)