Downloading the dataset -
Dataset_imagenet.ipynb 

Preparing the dataset - 
Data_loader.ipynb removes the black and white images
Image_editing.ipynb changes the images to blemished,blurred and noisy images.

We took the data from ImageNet, since there are 14M images, we just took a subset of the same from HuggingFace. More, info can be found in the above 
mentioned files and the final report.

Models :

Firstl, we built a Fully Connected Autoencoder model. The basic idea behind an autoencoder is to encode an input image into a compressed representation 
and then decode the compressed representation back into an output image that is similar to the original input image

Secondly, we will implement a Convolutional Neural Network on all three cases of image restoration. 
CNNs are considered to perform better with images as its built-in convolutional layer reduces the high dimensionality of images without losing its information.

CNN performed way better as supposed to autoencoder. You can run the models in models.ipynb. 

Note : the data is very big, so the models are going to run for a longer period of time.

Architecture of the models:

1. autoencoder_simple.png
2. conv.png

Testing:

If you just want to run the model - please download the file from - 
https://drive.google.com/file/d/1pC1fcT0n8FG2LrKk0tTppfPHl_gZAnHv/view?usp=sharing

And run the following code :

#from keras.models import load_model

#simple_auto = load_model('conv_auto.h5')

#predictions = simple_auto.predict('path to test images')

