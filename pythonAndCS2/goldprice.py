
kyat = input('Kyat: ')
kyat = int(kyat)

pae = input('Pae: ')
pae = int(pae)

yway = input('Yway: ')
yway = int(yway)

price_per_kyat = input('Price per kyat: ')
price_per_kyat = int(price_per_kyat)

gold_weight_in_kyats = kyat + (pae/16) + (yway/128)
gold_price = gold_weight_in_kyats * price_per_kyat

print(f'Total gold  price is {gold_price} kyats')
