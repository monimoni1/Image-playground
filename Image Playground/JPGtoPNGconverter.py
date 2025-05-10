import sys
import os
from PIL import Image
from pathlib import Path

#img = Image.open(./Pokedex/pikachu.jpg') #figure out a way to make the pikachu.jpg iterable





#class jpgtopng:
   # def __init__(self):
    #    self.name = name

   # def image
# using sys module we will grab 'Pokedex' and 'New' arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new exists and if not create
if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)
print(image_folder, output_folder)

# loop through pokedex convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name=os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

# save to the new folder