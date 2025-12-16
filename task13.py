# Write a Python function that takes a dictionary of items and their prices as input and finds and prints the keys (items) with the highest prices.

def highest_price(items_dict):
    
    h_price = None
    h_priced_items = []

    for item in items_dict:
        price = items_dict[item]
        
        
        if h_price is None or price > h_price:
            h_price = price
            h_priced_items = [item] 
        elif price == h_price:
            h_priced_items.append(item)
    print("Highest Price: ", h_price)
    print("Items with the highest price:", h_priced_items)

items = {'Apple': 85.50, 'Banana': 55.50, 'Orange': 90.50, 'Mango': 90.00, 'Grapes': 70.50}
highest_price(items)
