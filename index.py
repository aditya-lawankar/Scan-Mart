from flask import Flask, render_template, request, redirect, flash, url_for
import main
import urllib.request
from app import app
from werkzeug.utils import secure_filename
from main import getPrediction
import os
grocery_dict={"Apple Braeburn": 0, "Apple Crimson Snow": 1, "Apple Golden 1": 2, "Apple Golden 2": 3, "Apple Golden 3": 4, "Apple Granny Smith": 5, "Apple Pink Lady": 6, "Apple Red 1": 7, "Apple Red 2": 8, "Apple Red 3": 9, "Apple Red Delicious": 10, "Apple Red Yellow 1": 11, "Apple Red Yellow 2": 12, "Apricot": 13, "Avocado": 14, "Avocado ripe": 15, "Banana": 16, "Banana Lady Finger": 17, "Banana Red": 18, "Beetroot": 19, "Blueberry": 20, "Cactus fruit": 21, "Cantaloupe 1": 22, "Cantaloupe 2": 23, "Carambula": 24, "Cauliflower": 25, "Cherry 1": 26, "Cherry 2": 27, "Cherry Rainier": 28, "Cherry Wax Black": 29, "Cherry Wax Red": 30, "Cherry Wax Yellow": 31, "Chestnut": 32, "Clementine": 33, "Cocos": 34, "Corn": 35, "Corn Husk": 36, "Cucumber Ripe": 37, "Cucumber Ripe 2": 38, "Dates": 39, "Eggplant": 40, "Fig": 41, "Ginger Root": 42, "Granadilla": 43, "Grape Blue": 44, "Grape Pink": 45, "Grape White": 46, "Grape White 2": 47, "Grape White 3": 48, "Grape White 4": 49, "Grapefruit Pink": 50, "Grapefruit White": 51, "Guava": 52, "Hazelnut": 53, "Huckleberry": 54, "Kaki": 55, "Kiwi": 56, "Kohlrabi": 57, "Kumquats": 58, "Lemon": 59, "Lemon Meyer": 60, "Limes": 61, "Lychee": 62, "Mandarine": 63, "Mango": 64, "Mango Red": 65, "Mangostan": 66, "Maracuja": 67, "Melon Piel de Sapo": 68, "Mulberry": 69, "Nectarine": 70, "Nectarine Flat": 71, "Nut Forest": 72, "Nut Pecan": 73, "Onion Red": 74, "Onion Red Peeled": 75, "Onion White": 76, "Orange": 77, "Papaya": 78, "Passion Fruit": 79, "Peach": 80, "Peach 2": 81, "Peach Flat": 82, "Pear": 83, "Pear 2": 84, "Pear Abate": 85, "Pear Forelle": 86, "Pear Kaiser": 87, "Pear Monster": 88, "Pear Red": 89, "Pear Stone": 90, "Pear Williams": 91, "Pepino": 92, "Pepper Green": 93, "Pepper Orange": 94, "Pepper Red": 95, "Pepper Yellow": 96, "Physalis": 97, "Physalis with Husk": 98, "Pineapple": 99, "Pineapple Mini": 100, "Pitahaya Red": 101, "Plum": 102, "Plum 2": 103, "Plum 3": 104, "Pomegranate": 105, "Pomelo Sweetie": 106, "Potato Red": 107, "Potato Red Washed": 108, "Potato Sweet": 109, "Potato White": 110, "Quince": 111, "Rambutan": 112, "Raspberry": 113, "Redcurrant": 114, "Salak": 115, "Strawberry": 116, "Strawberry Wedge": 117, "Tamarillo": 118, "Tangelo": 119, "Tomato 1": 120, "Tomato 2": 121, "Tomato 3": 122, "Tomato 4": 123, "Tomato Cherry Red": 124, "Tomato Heart": 125, "Tomato Maroon": 126, "Tomato Yellow": 127, "Tomato not Ripened": 128, "Walnut": 129, "Watermelon": 130}
# list out keys and values separately
key_list = list(grocery_dict.keys())
val_list = list(grocery_dict.values())
 
# print key with val 100


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            label= getPrediction(filename)
            position = val_list.index(label)
            flash(key_list[position])
            return redirect('/')


if __name__ == "__main__":
    app.run()