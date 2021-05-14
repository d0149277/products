import os # operating system作業系統(要詢問電腦裡有沒有某個檔案)
def read_file(filename):# 讀取檔案
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品名稱,商品價格' in line:
				continue #繼續(跳過目前迴圈)
			name, price = line.strip().split(',') #只要遇到','就切割
			products.append([name, price])
	return products 

#讓使用者輸入及建立清單
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':#quit
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	print(products)
	return products
#印出所有購買紀錄
def print_products(products):
	for product in products: # 這是存取products清單
		print(product[0], '的價格是', product[1])
		#有增加或任何改變才需要return回傳

#寫入檔案(儲存)
def write_file(filename, products): # 由於products沒有宣告，所以需要給個參數
	with open(filename, 'w') as f:
		f.write('商品名稱,商品價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')
			

# 只有這裡開始執行 # 也會寫成沒有參數的function
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):# 不會重複使用  不需要寫成function
			print('yeah!找到檔案了!')
			products = read_file(filename) # 參數選擇products.csv
			print(products)
	else:
			print('Sorry,找不到檔案!')

	products = user_input(products)
	print_products(products)  #上面有return才需要 等於
	write_file('products.csv', products)
main() #要記得寫一個按下這個按鈕的動作