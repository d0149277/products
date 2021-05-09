products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':#quit
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

for product in products:
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w') as f:
	f.write('商品名稱,商品價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')