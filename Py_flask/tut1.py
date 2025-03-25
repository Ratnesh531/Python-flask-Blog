from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index1.html')

@app.route('/about')
def about():
    name  = "ratnesh"
    return render_template('index.html',name = name)

if __name__ == '__main__':
    app.run(debug=True,port = 5001)

