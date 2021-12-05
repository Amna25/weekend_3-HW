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


           
