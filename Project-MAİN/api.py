import os
check = None

try :
	import wget
	import numpy
	import keras
	import imutils
	import cv2

except :
	print("wait for downoading ")

	os.system("pip install wget")

	os.system("pip install numpy")

	os.system("pip install keras")

	os.system("pip install opencv-python")

	os.system("pip install argparse")

	os.system("pip install matplotlib")

import wget


if not os.path.isfile(os.path.join("face_detector")):
	check = True

	print("missing caffemodel and prot model  files are downloading .")

	wget.download("https://www.dropbox.com/sh/3uycobop07d1q12/AAA1T-7yysnr1nPIWHs-5XIba?dl=1")


if not os.path.isfile(os.path.join("model2-h5")):

	pcheck = True

	print("missing trained model(belongs to mertseven) file downloading .")

	wget.download("https://www.dropbox.com/s/b201z4c7xk2svdy/model2-h5?dl=1")
