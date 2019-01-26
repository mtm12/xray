from keras.models import load_model
import tensorflow as tf
import numpy as np
import pandas as pd
import ip_address
from flask import Flask, abort, jsonify, request
from PIL import Image, ImageFilter
import base64
import io

app = Flask(__name__)
xrayModel = None


def testFunc():
	z="1"
	return z
@app.route("/xray/api", methods=['POST'])
def make_predict():
	data = request.get_json(force=True)
	predict_request = data['image']
	#print(predict_request)
	#b64data = base64.encodestring(open("mnist/digit2.png","rb").read())
	#print("predict request")
	#predict_request_split = predict_request.split(',')[1]
	#print(predict_request_split)
	decoded_image = Image.open(io.BytesIO(base64.b64decode(predict_request.split(',')[1])))
	#print("end predict request")
	#decoded_image.save("xray/image.png")
	image250 = decoded_image.resize((250,250),Image.ANTIALIAS)
	rgbimg = Image.new("RGB", image250.size)
	rgbimg.paste(image250)
	imgData = np.asarray(rgbimg)
	imgData = imgData/255
	#image250.save("xray/image250.png")
	#img_data = np.asarray(imgData)
	img_data = imgData.reshape(250,250,3)
	print(img_data.shape)
	img_data = np.expand_dims(img_data, axis=0)
	prediction = xrayModel.predict(img_data)
	print(prediction)
	#print(prediction[0][0])
	#print("b64data")
	#print(b64data)
	#print("end b64data")
	#print("decoded image")
	#print(decoded_image)
	#y_pred = testFunc()
	#data = imageprepare(decoded_image)
	#data = imageprepare(b64data)
	#data = imageprepare('./mnist/digit2.png')
    #print(data)
	#tv = list(decoded_image.getdata())
	#y = np.array(tv)
	#z = y[:,3:]
	#y = z.reshape(28, 28)
	#y = np.expand_dims(y, axis=0)
	#y = np.expand_dims(y, axis=3)
	#print(y.shape)
	#print(data)
	
	#predict_request = np.array([predict_request])
	#predictions = mnistModel.predict(y)
	#print(predictions)
	##predictions_class = np.argmax(predictions[0],axis=0)
	#print(predictions_class)
	#probability = predictions[0][predictions_class]
	#print(probability)
	#predictions_class
	#data = imageprepare(predict_request)
	#a = "OK"
	return jsonify({'normal': str(prediction[0][0]), 'pneumonia': str(prediction[0][1])}), 201
	#a = "20"
	#return jsonify({'value': a}), 201


	
@app.route("/test/api")
def hello():
	a = "20"
	return jsonify({'value': a}), 201

if __name__=='__main__':
	print("loading xray model")
	xrayModel = load_model('./xray/tf_weights2-2-3.hdf5')
	print("xray model loaded")
	app.run(host=ip_address.ip_address, port=5002)