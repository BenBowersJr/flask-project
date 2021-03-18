from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
cartIds = []
store_inventory = [
  {
    'id': '1',
    'name': 'Jeans',
    'price': '$19.99',
    'description': 'the greatest first item'
  },
  {
    'id': '2',
    'name': 'Shirt',
    'price': '$39.99',
    'description': 'the greatest first item'
  },
  {
    'id': '3',
    'name': 'Hat',
    'price': '$19.99',
    'description': 'the greatest first item'
  }
]

#This just redirects to storepage untill i make a homepage
@app.route('/')
def home_page(): 
  return redirect(url_for('store_page'))

#Store page
@app.route("/store")
def store_page():
  return render_template('store.html', inv=store_inventory)

#Product page
@app.route('/store/<string:product>', methods=['POST', 'GET'])
def item_page(product):
  for item in store_inventory:
    # if we got here from a post method
    if request.method == 'POST':
      return render_template('product.html', itemName=item['name'], itemPrice=item['price'], itemContent=item['description'], itemID=item['id'])
    # otherwise display product page
    elif item['name'] == product:
      return render_template('product.html', itemName=item['name'], itemPrice=item['price'], itemContent=item['description'], itemID=item['id'])

@app.route('/store/<string:product>/add', methods=['POST'])
def add_to_cart(product):
  productID = request.form['ID']
  cartIds.append(productID)
  return redirect(url_for('store_page'))


# cart
@app.route('/cart')
def cart():
  return render_template('cart.html')



if __name__ == '__main__': 
  app.run(debug=True)