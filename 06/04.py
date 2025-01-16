# Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.
food_prices = [("Pizza", 12), ("Burger", 5), ("Pasta", 8), ("Salad", 3)]
sorted_food_prices = sorted(food_prices, key=lambda x: x[1], reverse=True)

print("Sorted food items by price:", sorted_food_prices)
