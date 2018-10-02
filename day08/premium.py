# premium.py
from member import Member
# Data(DB, 회원데이터) <-> Premium
# Entity
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
p1.add_cart(Item('키보드',1000,1))
p1.add_cart(Item('모니터',100000,1))
p1.purchase_from_cart()