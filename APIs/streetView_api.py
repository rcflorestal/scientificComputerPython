import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# define the params for the request
lat = 39.666842910869185
lng = -104.87146404657902
my_api_key = 'AIzaSyBAHAM5NC9xTDEMOeE1fAKJE5PSHcZWHMA'
link = f'https://maps.googleapis.com/maps/api/streetview?size=650x400&location={lat},{lng}&fov=80&heading=70&pitch=0&key={my_api_key}'

# request
req = requests.get(link)

print(req)

# Writing the picture to local disk and display it
with open('view.jpg', 'wb') as file:
        file.write(req.content)

req.close()

# using matpltolib to display the image
plt.figure(figsize=(10, 10))
img = mpimg.imread('view.jpg')
imgplot = plt.imshow(img)
plt.show()
