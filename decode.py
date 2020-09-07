#decode image in image

from PIL import Image
import tools

encoded_img = Image.open("encoded.jpg")
encoded_bitmap = encoded_img.load()

final_img = Image.new(encoded_img.mode,encoded_img.size)
final_bitmap = final_img.load()


for i in range(encoded_img.size[0]):
    for j in range(encoded_img.size[1]):
        rgb = tools.int_to_bin(encoded_bitmap[i,j])
        r, g, b = rgb
        final_bitmap[i,j] = tools.bin_to_int((r[4:]+"0000",g[4:]+"0000",b[4:]+"0000"))

final_img.show()


