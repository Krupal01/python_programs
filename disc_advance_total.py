data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300},{'item': 'item1', 'amount':750}]

disc = {}

for i in data:
    if i['item'] in disc.keys():
        disc[i['item']] += i['amount']
    else:
        disc[i['item']] = i['amount']

print(disc)