from flask import Flask, render_template, request
import os

__author__ = 'Todd Robbins'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# https://www.youtube.com/watch?v=bxFaa_FNdL4
@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'csv/')
    print(target)
    if not os.path.isdir(target) :
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return render_template("complete.html")


if __name__ == '__main__':
    app.run(debug=True) #run(port=4555, debug=True)

#@app.route('/<user>')
#@app.route('/shopping')
#def shopping():
#    food = ["Cheese", "Tuna", "Beef"]
#    return render_template("GraphTwoDimensions.html", food=food)

# @ signifies a decorator - way to wrap a function and modifying its behavior
# @app.route('/profile/<name>')
# def index(name):
#    return render_template("index.html", name=name)


# @app.route('/bacon', methods=['GET', 'POST'])
# def bacon():
#    if request.method == 'POST':
#        return 'You are using POST'
#    else:
#        return "You are probably using GET"

# @app.route('/plot')
# def tuna():
#    return '<h2>Tuna is good</h2>'

# @app.route('/profile/<int:post_id>')
# def show_post(post_id):
#    return '<h2>Post Id %s<h2>' % post_id
