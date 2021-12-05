from flask import render_template ,redirect
from app import app
from models.item_list import items,add_new_item,delete_item
from models.item import Item
from flask import request


@app.route('/items')
def index():
    return render_template('index.html', title='Shopping', items=items)


@app.route('/items',methods=['POST'])
def add_item():
    name=request.form["name"]
    price=(request.form["price"])
    quantity=(request.form["quantity"])
    if request.form["bought"] == "True":
        bought=True
    elif request.form["bought"]== "False":
        bought=False
        
    new_item=Item(name,price,quantity,False)
    add_new_item(new_item)
    return render_template("index.html", title="Shopping", items=items)

    @app.route('/items', methods=["POST"])
    def delete(name):
        delete_item(name)
        return redirect('/items')

    cost=request.form["quantity"]* request.form["price"]
    quantity=int(request.form["quantity"])
    price= int(request.form["priec"])
    total-cost=price*quantity
    



   




