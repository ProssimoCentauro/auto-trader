class Order:
    def __init__(self = None, type = None, pair = None, price = None, tp = None, sl = None):
        self.type = type
        self.pair = pair
        self.price = price
        self.tp = tp
        self.sl = sl
    
    def print_info(self):
        print(f"type: {self.type} \n pair: {self.pair} \n price: {self.price} \n TP: {self.tp} \n SL: {self.sl}")

class Modify_price:
    def __init__(self = None, type = None, pair = None, old_price = None, new_price = None):
        self.type = type
        self.pair = pair
        self.old_price = old_price
        self.new_price = new_price
    def print_info(self):
        print(f"type: {self.type} \n pair: {self.pair} \n old_price: {self.old_price} \n new_price: {self.new_price}")

class Modify_sl:
    def __init__(self = None, type = None, pair = None, old_sl = None, new_sl = None):
        self.type = type
        self.pair = pair
        self.old_sl = old_sl
        self.new_sl = new_sl

class Modify_tp:
    def __init__(self = None, type = None, pair = None, old_tp = None, new_tp = None):
        self.type = type
        self.pair = pair
        self.old_tp = old_tp
        self.new_tp = new_tp

class Close_position:
    def __init__(self = None, type = None, pair = None, status = None, price = None):
        self.type = type
        self.pair = pair
        self.status = status
        self.price = price

class Cancel_order:
    def __init__(self = None, type = None, pair = None, price = None):
        self.type = type
        self.pair = pair
        self.price = price