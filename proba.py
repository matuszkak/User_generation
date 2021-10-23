import unicodedata

data = 'Szabó béláaáá145úúő'
normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
print(normal.decode("utf-8"))
