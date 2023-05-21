from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('index.html')

@app.route('/product')
def product():
    return 'Product page'

if __name__ == "__main__":
    app.run(debug=True, port=8000)