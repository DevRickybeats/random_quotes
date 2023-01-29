from flask import Flask, render_template
from quotes import quotes
import random



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quote', methods=['GET'])
def quote():
    quote = random.choice(quotes)
    return render_template('quote.html', quote=quote)

    

if __name__ == '__main__':
    app.run(debug=True)
