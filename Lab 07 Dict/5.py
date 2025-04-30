# Create two dictionaries – one containing grocery items and their prices and another containing
# grocery items and quantity purchased. By using the values from these two dictionaries compute
# the total bill.
def calculateTotalBill(groceryPrices, groceryQuantity):
    return sum(groceryPrices[item] * groceryQuantity[item] for item in groceryPrices)

groceryPrices = {"apple": 10, "banana": 5, "orange": 13}
groceryQuantity = {"apple": 5, "banana": 3, "orange": 2}

bill = calculateTotalBill(groceryPrices, groceryQuantity)
print(bill)