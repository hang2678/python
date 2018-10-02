# item.py
# 사전에 등록(DB)되어 있는 상품 데이터를 모델링
# private(__), public
class Item:
    def __init__(self, name, price, qty):
        self.__name = name
        self.__price = price
        self.__qty = qty

    def setname(self, n):
        self.__name = n
    def getname(self):
        return self.__name

    def setprice(self, p):
        self.__price = p
    def getprice(self):
        return self.__price

    def setqty(self, q):
        self.__qty = q
    def getqty(self):
        return self.__qty
    
--------------------------------------------
conn = pymysql.connect(...)
cursor = conn.cursor()
cursor.execute('SELECT * FROM ITEM WHERE category='PC')
db_list = cursor.fetchall() # list -> index item_list[0]
item_list = []
for item in db_list: 
    obj_item = Item(item['name'], item['price'], item['qty'])
    item_list.append(obj_item)

for product in item_list:
    print(product.name, product.price, product.qty)