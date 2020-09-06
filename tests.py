from PIL import Image
import tools

img = Image.open("minions.jpg")
bm = img.load()
#
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         rgb = tools.int_to_bin(bm[i,j])
#         r, g, b = rgb
#         bm[i,j] = tools.bin_to_int((r[:4]+'0000',g[:4]+'0000',b[:4]+'0000'))
#
# img.show()


a = (123,222,78)
b = (45,111,47)
x = tools.int_to_bin(a)
y = tools.int_to_bin(b)
print(tools.bin_to_int(x),tools.bin_to_int(y))
print(tools.int_to_bin(a))
print(tools.int_to_bin(b))
va = tools.add_rgb(x,y)
r, g, z = va
vv = (r[4:]+"0000",g[4:]+"0000",z[4:]+"0000")
print(tools.add_rgb(x,y))
print(va)
print(vv)
print(a,b)
print(tools.bin_to_int(vv))