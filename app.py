from flask import Flask,render_template, jsonify
app = Flask(__name__)

from product import products
@app.route('/ping')
def home():
    return jsonify({'message':"pong!"})

@app.route('/products')
def getproducts():
    return jsonify({'product':products,"message":"producto"})

if __name__==('__main__'):
    app.run(debug=True, port=4000)