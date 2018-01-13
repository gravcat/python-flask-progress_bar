import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('progress_bar.html', progress=22)

if __name__ == '__main__':
    # bind to env/heroku provided port, otherwise default 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, port=port)
