import PIL as pillow
from PIL import Image
import colorama # yay colorful
import time
import math

GRAYSCALE_ASCII = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.   "

colorama.init(autoreset=True)
CYAN = colorama.Fore.CYAN
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
RESET = colorama.Style.RESET_ALL

image_name = input("Choose file name: " + CYAN)
print(RESET, end="")

start_time = time.time()

try:
    with Image.open(image_name) as img:
        img.load()
except:
    print(f"{RED}[ERROR]{RESET} Incorrect file name")
    exit(0)

# resize the image to 50x50
sizes = img.size
scale_x = sizes[0] / 100
scale_y = sizes[1] / 50

img = img.resize((round(img.width/scale_x), round(img.height/scale_y)))
img = img.convert("L")

# get the data and convert it to a 2D array
pixels = img.getdata()

new_pixels = []
for x in range(img.height):
    new_pixels.append([])
    for y in range(img.width):
        new_pixels[x].append(pixels[x * img.width + y])

pixels = new_pixels
del new_pixels # we don't need it anymore

# begin printing
for row in pixels:
    for col in row:
        print(GRAYSCALE_ASCII[round(col/256*len(GRAYSCALE_ASCII))-1], end="")
    print() # new line

def convert_seconds_to_time(seconds):
    lm, ls = divmod(seconds,60)
    lh, lm = divmod(lm, 60)
    ls, lm, lh = math.floor(ls), math.floor(lm), math.floor(lh)
    str_lm = str(lm)
    if lh >= 1:
        if lm < 10:
            str_lm = "0" + str(lm)
    if ls < 10 and lm >= 1:
        ls = "0" + str(ls)

    return f"{str(lh) + 'h' if int(lh) != 0 else ''}{str_lm + 'm' if int(lm) != 0 else ''}{ls}.{str(float(seconds)-math.floor(seconds))[-3:]}s"

print(f"\n{GREEN}[INFO]{RESET} Took {convert_seconds_to_time(round(time.time()-start_time, 3))}")