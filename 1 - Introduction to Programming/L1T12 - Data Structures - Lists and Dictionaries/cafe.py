# List the cafe's menu items
# Assign the total stock values in the list
# Assign stock unit price
menu = ["Pies", "Cooldrink", "Samoosas", "Coffee"]
stock = {"Pies": 100,
          "Cooldrink": 200,
          "Samoosas": 200, 
          "Coffee": 200}
price = {"Pies": 25, 
         "Cooldrink": 10, 
         "Samoosas": 5, 
         "Coffee": 15}

# Use for loop to calculate the total value of the worth of stock in list
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Print the result
print("The Cafe's total stock is worth: R", (total_stock_worth))
