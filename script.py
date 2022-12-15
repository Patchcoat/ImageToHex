from PIL import Image
import math

def w_or_b(pixel):
    if pixel[0] == 255:
        return 0
    else:
        return 256

def get_bank(px, col, row):
    bank_value = 0x0
    for i in range(0, 8):
        bank_value = bank_value | w_or_b(px[row, col+i])
        bank_value = bank_value >> 1
    return bank_value

file = open("Output.txt", "w")

im = Image.open(r"Input.png")
px = im.load()
file.write("{")
for col in range(0,6):
    for row in range(0,84):
        bank_value = get_bank(px, col*8, row)
        file.write(format(bank_value, '#x') + ", ")
    file.write("\n")
file.write("};\n")
file.close();
