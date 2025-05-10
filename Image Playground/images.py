from PIL import Image, ImageFilter
img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SHARPEN)
filtered_img3 = img.filter(ImageFilter.SMOOTH)
filtered_img4 = img.convert('L')
print(img) #shows us that this oobject exsists
print(img.size) # shows pixel sizes i think
print(img.mode) # shows the mode of image

filtered_img.save("blur.png", 'png')
filtered_img2.save("sharp.png", 'png')
filtered_img3.save("smooth.png", 'png')
filtered_img4.save("grey.png", 'png')

filtered_img4.show()