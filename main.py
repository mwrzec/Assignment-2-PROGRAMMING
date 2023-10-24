from ast import While
from app import Product
"""
main function that runs sim
"""
def main():
    print("Welcome to Marcel's Product Stock Simulation")

    code = int(input("Enter the Product Code (100-1000):  "))
    name = input("Enter the Name of the Product:  ")
    price = float(input("Enter the Product Price:  "))
    cost_to_make = float(input("Enter the Manufacturer Cost:  "))
    """
    while loop to ensure stock > 0
    """
    while True:
        current_stock = int(input("Enter the Current Stock:  "))
        if current_stock > 0:
            break
        else:
            print("Stock Amount must be greater than 0. Please try again.")
    
    monthly_units = int(input("Enter the Monthly amount of Units Manufactured:  "))
    months = 12

    product = Product(code, name, price, cost_to_make, current_stock, monthly_units)

    product.stock_statement(months)
    """
    display statement
    """
    print("Monthly Stock Statement: ")
    totalprofit = 0
    totalloss = 0
    tnetprofit = 0
    """
    display summary
    """
    for monthly_data in product.monthly_data:
        month, manufactured, sold, stock, gain, loss, netgainloss = monthly_data
        totalprofit += gain
        totalloss += loss
        tnetprofit += netgainloss

        print(f"Month {month}: ")
        print(f"Manufactured {manufactured}")
        print(f"Sold {sold}")
        print(f"Stock {stock}")
        print(f"Sales Gain: ${gain:.2f}")
        print(f"Loss: ${loss:.2f}")
        print(f"Net Gain Loss: ${netgainloss:.2f}")
        print("-" * 30)

    print("Total: ")
    print(f"Total Profit: ${totalprofit:.2f}")
    print(f"Total Loss: ${totalloss:.2f}")
    print(f"Total Net Profit: ${tnetprofit:.2f}")

if __name__ == "__main__":
    main()