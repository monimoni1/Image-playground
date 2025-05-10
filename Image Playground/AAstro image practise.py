from PIL import Image, ImageFilter

img = Image.open('./astro.jpeg')

print(img.size)

new_img = img.resize(400,400) #however this will squish images to fit the 1:1 aspect ratio.
new_img.save('thumbnail.jpg')

new_img2 = img.thumbnail(400,400)
new_img2.save('thumbnail2.jpg') #keeps the aspect ratio. .thumbnail is the function

print(new_img2.size())