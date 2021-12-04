from models.item import *


item1=Item("milk", 20 ,2, True)
item2=Item("bread",10 ,1 , False)
items=[item1, item2]


def add_new_item(item):
    items.append(item)



def delete_item(item_name):
    item_to_delete=None
    for item in items:
        if item.name==item_name:
            item_to_delete = item
            break
        items.remove(item_to_delete)

# def total_cost(price, quantity):
#     total_price=items.price
#     total_quantity=items.quantity
#     if total_price * total_quantity == total_cost:
#         total_cost(price*quantity)


