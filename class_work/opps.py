class shopping :
    discount=10
    def product(self,price,name):
        self.price=price
        self.name=name
user1=shopping()
user2=shopping()
user1.product(34000,'laptop')
user2.product(56000,'phone')
print(user1.price)
print(shopping.discount)
print(user2.price)
