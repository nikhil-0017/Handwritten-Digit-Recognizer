from PIL import Image 
img=Image.open('five1.png')
data=list(img.getdata())
for i in range(len(data)):
    data[i]=255-data[i]
print(data)

