import operator

items=[("Burger",99),("Pizza",199),("Tacos",49)]
sorted_items = (sorted(items, key = operator.itemgetter(1),reverse=True))
print(sorted_items)