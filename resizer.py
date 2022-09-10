from PIL import Image
import os

input_path = ""
output_path = "" #example: C:\\Users\\lucaa\\Desktop\\travel\\resized\\

for filename in os.listdir(input_path):
    image = Image.open(filename)
    exif = image.info['exif']
    new_image = image.resize((3984, 2656)) # change resolution
    new_image.save(output_path + filename, exif = exif)
    
    
print("Done!")

