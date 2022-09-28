from flask import Flask

UPLOAD_FOLDER = 'C:\\Users\\lawan\\Desktop\\projects\\fruit-detection\\Scan-Mart\\test_images'

app = Flask(__name__,template_folder='template',static_folder='static')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER