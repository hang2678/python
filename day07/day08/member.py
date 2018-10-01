# member.py
class Member:
    def __init__(self, name, id, pwd):
        self.name = name
        self.id = id
        self.pwd = pwd
        self.point = 0
        self.total_amount = 0
        self.cart = []

    def getpoint(self):
        return self.point
    
    def setpoint(self, point):
        self.point += point

    def gettotal_amount(self):
        return self.total_amount
    
    def settotal_amount(self, amount):
        self.total_amount += amount

    def login(self, id, pwd):
        print('{0}로 로그인 되었다.'.format(id))
        # DB check with ID, PWD

        pass
    
    def logout(self, id):
        print('{0}님이 로그아웃 되었다.'.format(id))
        pass

    def search_items(self, search_keyword):
        # DB search with keyword
        return "상품의 목록을 전달합니다."

    def add_cart(self, item):
        self.cart.append(item)

    def purchase_from_cart(self):
        for item in self.cart:
            self.purchase_direct(item)

    def purchase_direct(self, item):
        # 1. 재고 파악 -> 업데이트
        # 2. 결제
        # 3. 포인트 처리 (적립, 사용...)
        # 4. 상품 상태를 변경 (준비중, 발송중, 배송중, 배송완료)
        #    준비중 상태로 설정
        self.point += 10 * 0.05
        self.total_amount += 1000
        self.purchased_list.append(item)
        pass

    def get_purchased_list(self):
        for item in self.purchased_list:
            print('구매 목록:', item)