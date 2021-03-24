from app import app
from flask import render_template
from models.curry_in_a_hurry import food_menus

@app.route("/food_menu")
def index():
    return render_template('index.html', title="Home", food_menus=food_menus)

@app.route('/food_menu/<index>')
def show(index):
    return render_template('show.html', food_menu=food_menus[int(index)])

