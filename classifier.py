import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import joblib


def classify(address):
  # Disable scientific notation for clarity
  np.set_printoptions(suppress=True)

  # Load the model
  model = tensorflow.keras.models.load_model('keras_model.h5')
  # print(model)
  # Create the array of the right shape to feed into the keras model
  # The 'length' or number of images you can put into the array is
  # determined by the first position in the shape tuple, in this case 1.
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  # Replace this with the path to your image
  # Image path from the drag and drop code.
  image = Image.open(address).convert('RGB')

  #resize the image to a 224x224 with the same strategy as in TM2:
  #resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.ANTIALIAS)

  #turn the image into a numpy array
  image_array = np.asarray(image)

  # display the resized image
  # image.show()

  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

  # Load the image into the array
  data[0] = normalized_image_array

  # run the inference
  prediction = model.predict(data)
  # print(prediction)

  new = str(prediction)
  # print(new)
  new = new.replace('[','')
  new = new.replace(']','')
  length = len(new)
  # print(length)
  new1 = new
  elliptical_galaxy = ""
  irregular_galaxy = ""
  spiral_galaxy = ""
  star = ""
  nebula = ""
  black_hole = ""
  planets = ""
  moon = ""
  for i in range(0,length):
    if new[i]==" ":
      j=i
      new = new[j:length]
      new = new.strip()
      break
    else:
      elliptical_galaxy = elliptical_galaxy + new[i]
  # print(elliptical_galaxy)
  # print(new)
  length = len(new)
  for i in range(0,length):  
    if new[i]==" ":
      j=i
      new = new[j:length]
      new = new.strip()
      break
    else:
      irregular_galaxy = irregular_galaxy + new[i]
  # print(irregular_galaxy)
  length = len(new)
  for i in range(0,length):
    if new[i]==" ":
      j=i
      new = new[j:length]
      new = new.strip()
      break
    else:
      spiral_galaxy = spiral_galaxy + new[i]

  # print (stars)
  length = len(new)
  for i in range(0,length):
    if new[i]==" ":
      j=i
      new = new[j:length]
      new = new.strip()
      break
    else:
      star = star + new[i]

  # print (nebula)
  length = len(new)
  for i in range(0,length):
    if new[i]==" ":
      j=i
      new = new[j:length]
      new = new.strip()
      break
    else:
      nebula = nebula + new[i]

  # print (black_hole)
  length = len(new)
  for i in range(0,length):
    if new[i]==" ":
      j=i
      new = new[j:length]
      new = new.strip()
      break
    else:
      black_hole = black_hole + new[i]
      
  # print (planets)
  length = len(new)
  for i in range(0,length):
    if new[i]==" ":
      j=i
      new = new[j:length]
      new = new.strip()
      break
    else:
      planets = planets + new[i]

  # print (moon)
  length = len(new)
  for i in range(0,length):
    if new[i]==" ":
      j=i
      new = new[j:length]
      new = new.strip()
      break
    else:
      moon = moon + new[i]
      
  # Find greatest of all results
  def detection(type):
    return max(type, key=type.get)

  a = detection({"Elliptical Galaxy":elliptical_galaxy,"Irregular Galaxy":irregular_galaxy, 
                        "Spiral Galaxy":spiral_galaxy, "Star":star, 
                        "Nebula":nebula,"Black Hole":black_hole,"Planet":planets,"Moon":moon})



  # confidence percent of algoritm
  confidence = [elliptical_galaxy,irregular_galaxy,spiral_galaxy,star,nebula,black_hole,planets,moon]
  confidence.sort()
  number = float(confidence[-1])
  percent = float(number*100)
  return('Object is a: '+str(a)+"\n Result returned with "+str(percent)+"%"+" Confidence")
  # here a is the result
  #print(a)






