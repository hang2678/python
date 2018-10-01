# premium.py
from member import Member

class Premium(Member):
    def purchase_direct(self, item):
        pass

p1 = Premium('이도원', 'user1', '123')
p1.login('user1', '123')
p1.logout('user1')
p1.setpoint(100)
print(p1.getpoint())
p1.setpoint(-50)
p1.search_items('노트북')
p1.add_cart('삼성노트북')
p1.add_cart('LG모니터')
p1.purchase_direct('키보드')
p1.purchase_from_cart()