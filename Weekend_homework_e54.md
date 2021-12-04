# Weekend Homework 

 ## :star: PDA Reminder :star: 

You should be able to complete a few of the new PDA assignments with this homework
- Wireframes
- Class Diagram
- Object Diagram 
- Psudeocode 

 ## Task

Your task is to model a Flask app which will list items on a shopping list and allow users to add items to the list.
Please remember to plan this homework before getting started. You could use the PDA to help plan and structure your code. 

### MVP
Your application should have a single class - Items - and should contain the following properties:

- Name of Item
- Price
- Quantity
- Bought?

Provide the following functionality:

- List all shopping list items
- Create a new item using a form.

### Extensions

- Have functionality to filter between bought and not bought items
- Calculate the total cost of the shopping list items.
- Display the total number of items in the shopping list.
- If the user buys a specific quantity of an item - apply a 10% discount.
- Style the app using CSS

### Advanced Extensions
- Delete the items from the list (either use index or item name to do this)
Because we can't use the DELETE HTTP method you will need to create a POST route to /items/delete/<index> in order to avoid conflicts!
- Anything else you can think of

#### Guidance

To style a Flask app you will need to put your CSS files inside a folder called `static` inside the `app` package.

Then add the following line inside the <HEAD> tag of your `base.html`

```html
    <link rel="stylesheet" href="{{ url_for('static', filename='your_file_name.css') }}">
```

When deleting the item use a form and the event name to identify which one is to be deleted.

An HTML checkbox input value will only be included in the form dictionary if the box is checked. It will by default return the string 'On'
