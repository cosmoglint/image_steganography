#just a prompt for flipping images
def yes_or_no(question):
    while 1:
        reply = str(raw_input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y' :
            return True
        if reply[0] == 'n':
            return False
        else:
            return yes_or_no("enter yes or no pls")
            yes_or_no("would you like to flip images?")

def int_to_bin(rgb):
    #tuple rgb value
    #this cool method adopted from kevin
    r, g, b = rgb
    return ("{0:08b}".format(r),"{0:08b}".format(g),"{0:08b}".format(b))

def bin_to_int(rgb):
    #tuple rgb in binary
    r, g, b = rgb
    return (int(r,2),int(g,2),int(b,2))

def add_rgb(rgb1,rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return (r1[:4]+r2[:4], g1[:4]+g2[:4], b1[:4]+b2[:4])