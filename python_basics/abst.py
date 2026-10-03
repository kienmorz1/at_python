from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class CardPayment(Payment):
    def pay(self):
        print("Swipped")
    
    def get_card_num(self):
        print("5858585885858")

class UpiPayment(Payment):
    def pay(self):
        print("Paytm karo!!")
    def get_upi_id(self):
        print('gankri31@okaxis')


def payment_type(obj):
    obj.pay()

for obj in [CardPayment(),UpiPayment()]:
    payment_type(obj)

upi = UpiPayment()
card = CardPayment()
upi.get_upi_id()
card.get_card_num()