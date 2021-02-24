#steganography image in image

from PIL import Image
import tools

#cant encode larger image in smaller
main_img = Image.open("embed.jpg")
msg_img = Image.open("main.jpg")

# def merge_files(main_img,msg_img):
if msg_img.size[0] > main_img.size[0] or msg_img.size[1] > main_img.size[1]:
    print("image 1 size is smaller than image 2 size")
    inpu = tools.yes_or_no("would you like to flip images?")
    if inpu:
        main_img , msg_img = msg_img, main_img
        print("images flipped")
    else:
        print("okay use some other image, bye")
        exit(1)

bitmap_main = main_img.load()
bitmap_msg = msg_img.load()

final_image = Image.new(main_img.mode,main_img.size)
bitmap_final = final_image.load()

for i in range(main_img.size[0]):
    for j in range(main_img.size[1]):
        rgb1 = tools.int_to_bin(bitmap_main[i, j])
        if i<msg_img.size[0] and j<msg_img.size[1]:
            rgb2 = tools.int_to_bin(bitmap_msg[i,j])
        else:
            rgb2 = tools.int_to_bin((0,0,0))

        fin_rgb = tools.add_rgb(rgb1,rgb2)
        bitmap_final[i,j] = tools.bin_to_int(fin_rgb)

final_image.show()
final_image.save("encoded.jpg")
