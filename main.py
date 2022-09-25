
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import  load_model
from PIL import Image
import numpy as np


#Loading the image 

 

def getPrediction(filename):

    model=load_model('model.h5')
    np_image = Image.open('uploads/'+filename)
    np_image=np_image.resize((100,100))
    np_image = np.array(np_image).astype('float32')/255
    np_image = np.expand_dims(np_image, axis=0)
 
    prediction = (np.argmax(model.predict(np_image), axis=-1))
    return int(prediction[0])
   