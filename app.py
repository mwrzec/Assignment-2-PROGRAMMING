import random

class Product:
    def __init__(self,prodcode,name,sale_price,manufacture_cost,stock,monthly_units):
        self.prodcode = prodcode 
        self.name = name
        self.sale_price = sale_price
        self.stock = stock
        self.manufacture_cost = manufacture_cost
        self.monthly_units = monthly_units
        self.monthly_data = []
        
    def product_sale_month(self):
        units_made = self.monthly_units
        unit_sales = random.randint(units_made - 10,units_made + 10)
        unit_sales = min(unit_sales, self.stock)
        self.stock -= unit_sales

    def stock_statement(self,months):
        for month in range(1, months + 1):
            unit_sales  = self.product_sale_month()
            self.stock += self.monthly_units - unit_sales
            profit = unit_sales * self.sale_price
            loss = unit_sales * self.manufacture_cost
            totalprofit = profit - loss
            self.monthly_data.append((month, self.monthly_units, unit_sales, self.stock, profit, loss, totalprofit))


