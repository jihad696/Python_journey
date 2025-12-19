my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []


for data in zip(my_list, my_tuple):
    my_data.append(str(data[0]))
    my_data.append(str(data[1]))

final_string = "".join(my_data)
print(final_string)  # Elzero

# #=========================================
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if type(item1) == str:
        my_data.append(item1)
    else:
        continue

final_string = "".join(my_data)


print(final_string)

# # ======================================
from PIL import Image

img = Image.open('/home/gehad/PycharmProjects/PythonProject1/PythonProject/PythonProject/elzero_pyhton/86-89/elzero-pillow.png')

width, height = img.size
block_width = width // 3
block_height = height // 2

l_block = img.crop((block_width, 0, block_width * 2, block_height))
l_gray = l_block.convert('L')
l_gray.save('L_gray.png')

r_block = img.crop((block_width, block_height, block_width * 2, height))
r_gray = r_block.convert('L')
r_gray.save('R_gray.png')

o_block = img.crop((block_width * 2, block_height, width, height))
o_gray = o_block.convert('L')
o_gray.save('O_gray.png')

bottom_part = img.crop((0, block_height, width, height))
gray_bottom = bottom_part.convert('L')
rotated_bottom = gray_bottom.rotate(180)
rotated_bottom.save('bottom_rotated.png')

print("Done!")
# =============================================
# Write Function With Help To Get The Output

def say_hello_to(name):
    """
    "parameter(someone) => Person Name"
    "Function To Say Hello To Anyone"
    """

    return f"Hello {name}"

print(say_hello_to("Osama")) # "Hello Osama"

# Write Doc String Line For The Function Here
print(say_hello_to.__doc__)

# Function Doc String Output
"parameter(someone) => Person Name"
"Function To Say Hello To Anyone"

# ====================================================
myFriends = ["Ahmed", "Osama", "Sayed"]

def sayHello(SomePeoples) -> list:
  for Someone in SomePeoples:
    print(f"Hello {Someone}")

sayHello(myFriends)


