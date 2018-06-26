from flask import Flask, render_template, request
import os
app = Flask(__name__)

# https://www.youtube.com/watch?v=bxFaa_FNdL4
@app.route('/')
def index():
    return render_template("index.html")

#@app.route('/<user>')
#@app.route('/shopping')
#def shopping():
#    food = ["Cheese", "Tuna", "Beef"]
#    return render_template("GraphTwoDimensions.html", food=food)


if __name__ == '__main__':
    app.run()

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
