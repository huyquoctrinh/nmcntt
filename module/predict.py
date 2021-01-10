import pickle
import numpy as np
import cv2
import sklearn
def test(img_path):
	path = './model/knn_model_vectorize.pkl'
	loaded_model = pickle.load(open(path, 'rb'))
	img= cv2.imread(img_path,cv2.COLOR_BGR2GRAY)
	img=cv2.resize(img,(28,28))
	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	cv2.imwrite('huy.jpg',img)
	img=np.array(img)
	# print(img.shape)
	img = img.reshape((28,28,1))
	# print(img.shape)
	img = img.reshape((28, 28)).astype("uint8")
	prediction = loaded_model.predict(img.reshape(1,-1))[0]
	return prediction
def test_gui(img):
	path = './model/knn_model_vectorize.pkl'
	loaded_model = pickle.load(open(path, 'rb'))
	# img= cv2.imread(img_path,cv2.COLOR_BGR2GRAY)
	img=cv2.resize(img,(28,28))
	# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	cv2.imwrite('huy.jpg',img)
	img=np.array(img)
	# print(img.shape)
	img = img.reshape((28,28,1))
	# print(img.shape)
	img = img.reshape((28, 28)).astype("uint8")
	prediction = loaded_model.predict(img.reshape(1,-1))[0]
	return prediction