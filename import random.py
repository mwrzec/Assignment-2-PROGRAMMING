import random

class Product:
    def __init__(self,prodcode,name,sale_price,manufacture_cost,stock,monthly_units):
        self.prodcode = prodcode 
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.monthly_units = monthly_units
        self.monthly_data = []
        