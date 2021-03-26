from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Cart.sqlite3'

###### NONE OF THIS IS USED, USED FOR TESTING ########
db = SQLAlchemy(app)

class Cart(db.Model):
  _id = db.Column("id", db.Integer, primary_key=True)
  quantity = db.Column(db.Integer)
  price = db.Column(db.Float(4, 2))

  def __init__(self, id_, quantity, price):
    self._id = id_
    self.quantity = quantity
    self.price = price 

###### NONE OF THIS IS USED, USED FOR TESTING ########


store_inventory = [
  {
    'id': '1',
    'name': 'Sweater',
    'price': '34.99',
    'image': 'sweater.jpeg'
  },
  {
    'id': '2',
    'name': 'Shirt',
    'price': '39.99',
    'image': 'shirt.jpg'
  },
  {
    'id': '3',
    'name': 'Hat',
    'price': '19.99',
    'image': 'hat.jpg'
  }
]

#This just redirects to storepage untill i make a homepage
@app.route('/')
def home_page(): 
  return redirect(url_for('store_page'))

@app.route('/clear', methods=['POST'])
def clear():
  session.clear()
  return render_template('cart.html')

@app.route('/addtocart', methods=['POST'])
def add_to_cart():
  #create new item dict
  newCartItem = { f"{request.form['id']}": {
    'name': request.form['name'], 
    'quantity': request.form['quantity'], 
    'price': request.form['price'],
    'image': request.form['image']
    }
  }
  #if there is a cart
  if 'cart' in session:
    #get every key in the cart
    for key in session['cart'].keys():
      # if the key is the same as the Product ID, dont add it to the cart
      if key == request.form['id']: 
        #tell the user and redirect
        flash('Item already in cart!')
        return redirect(url_for('store_page'))
    #This merges the new item with the current cart
    session['cart'] = session['cart'] | newCartItem
  else: 
    session['cart'] = newCartItem
  return redirect(url_for('store_page'))


#Store page
@app.route("/store", methods=['POST', 'GET'])
def store_page():
  return render_template('store.html', inv=store_inventory)

# cart
@app.route('/cart')
def cart():
  if 'cart' in session:
    return render_template('cart.html', cart=session['cart'], cartKeys=session['cart'].keys())
  else:
    return render_template('cart.html')

@app.route('/checkout', methods=['POST'])
def checkout():
  if request.method == 'POST':
    flash('Transaction has been processed')
  return redirect(url_for('cart'))



if __name__ == '__main__': 
  db.create_all()
  app.run(debug=True)