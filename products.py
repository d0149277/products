import os # operating system作業系統(要詢問電腦裡有沒有某個檔案)

products = []
if os.path.isfile('products.csv')
	print('yeah!找到檔案了!')
	with open('products.csv.', 'r') as f:
		for line in f:
			if '商品名稱,商品價格' in line:
				continue #繼續(跳過目前迴圈)
			name, price = line.strip().split(',') #只要遇到','就切割
			products.append([name, price])
	print(products)

else:
	print('Sorry,找不到檔案!')

#讓使用者輸入及建立清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':#quit
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

#印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

#寫入檔案(儲存)
with open('products.csv', 'w') as f:
	f.write('商品名稱,商品價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')