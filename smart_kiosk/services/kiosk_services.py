import uuid 
#from typing import List, Dict, Optional

#Query1: Place a new order for an item and quantity
#Query2: UView all orders placed for a particular item
#Query3: Find how many orders placed for the item using item id

def place_order():
    #find item 
    item= find_inventory_item_by_item_id(inventory_items, item_id)
    # check the existing inventory for the item
    if item:
        if item['quantity'] >= quantity:
            orders.append(
                {
                    'id': str(uuid.uuid4()),
                    'item_id': item_id,
                    'quantity': quantity
                }
            )
    #if we have enough inventory, then reduce the inventory
    #then place the order
   

def find_orders_by_item():
    pass

def count_orders_by_item():
    pass

def find_inventory_by_item_id(inventory_list: list, item_id:str): 
    for item in inventory_list:
        if item['id'] == item_id:
            return item
        
    return None

def update_inventory_item():
    pass