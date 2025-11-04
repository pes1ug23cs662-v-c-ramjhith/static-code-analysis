import json
from datetime import datetime

# Global variable
stock_data = {}

# Fix 1: Changed default logs=[] to logs=None (Mutable Default Argument)
# Fix 6: Renamed addItem to add_item
def add_item(item="default", qty=0, logs=None):
    """Adds a specified quantity of an item to the inventory."""
    # Fix 1: Initialize logs as a new list if None is passed
    if logs is None:
        logs = []
    
    # Optional: Basic input type validation
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Warning: Invalid input types for item or quantity: {item}, {qty}")
        return

    if not item:
        return
    
    stock_data[item] = stock_data.get(item, 0) + qty
    
    # Optional: Fix Pylint C0209 (Formatting with f-string)
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

# Fix 6: Renamed removeItem to remove_item
def remove_item(item, qty):
    """Removes a specified quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # Fix 2: Replaced bare except with specific KeyError
    except KeyError:
        print(f"Warning: Attempted to remove non-existent item: {item}")
        pass

# Fix 6: Renamed getQty to get_qty
def get_qty(item):
    """Returns the current stock quantity for an item."""
    # Added defensive check for KeyError
    return stock_data.get(item, 0)

# Fix 4 & 6: Used 'with open' for proper resource management and renamed loadData to load_data
def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file."""
    try:
        # Fix 4: Using 'with' statement
        with open(file, "r") as f:
            global stock_data
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        # Graceful handling if the file doesn't exist yet
        print(f"Inventory file not found: {file}. Starting with empty stock.")

# Fix 4 & 6: Used 'with open' for proper resource management and renamed saveData to save_data
def save_data(file="inventory.json"):
    """Saves inventory data to a JSON file."""
    # Fix 4: Using 'with' statement
    with open(file, "w") as f:
        f.write(json.dumps(stock_data))

# Fix 6: Renamed printData to print_data
def print_data():
    """Prints a report of all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")

# Fix 6: Renamed checkLowItems to check_low_items
def check_low_items(threshold=5):
    """Checks and returns a list of items below the specified threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    """Main execution function to demonstrate inventory system usage."""
    add_item("apple", 10)
    add_item("banana", -2)
    
    # Added defensive check/cast for invalid types
    add_item("123", 10) # Fixed invalid type use in the original
    
    remove_item("apple", 3)
    remove_item("orange", 1)
    
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    
    save_data()
    load_data()
    print_data()
    
    # Fix 3: Removed dangerous eval() call
    # eval("print('eval used')") 

main()