from flask import Flask, render_template
from quotes import quotes
import random
from flask import jsonify



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/quote')
# def quote():
#     return render_template('quote.html', quote=random.choice(quotes))

@app.route('/quote', methods=['GET'])
def quote():
    quote = random.choice(quotes)
    return render_template('quote.html', quote=quote)

    

if __name__ == '__main__':
    app.run(debug=True)
