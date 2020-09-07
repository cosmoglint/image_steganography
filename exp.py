from PIL import Image
import tools

img = Image.open("main.jpg")
img2 = Image.open("main copy.jpg")

img.show()

def show_msb(img):
    bm = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            rgb = tools.int_to_bin(bm[i,j])
            r,g,b = rgb
            rgb2 = (r[:4]+"0000",g[:4]+"0000",b[:4]+"0000")
            bm[i,j] = tools.bin_to_int(rgb2)

    img.show()

show_msb(img)
show_msb(img2)