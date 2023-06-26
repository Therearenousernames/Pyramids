import math
import sys

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    # create a list of valid shapes 
    # prints an error message if user input is invalid and prompts user input again.
    list_of_shapes = ['parallelogram', 'rectangle', 'pyramid', 'diamond', 'square', 'triangle']
    while True:
        shape = input("Shape?: ").lower()
        if shape in list_of_shapes:
            return shape
        elif shape not in list_of_shapes:
            print(f"User input: {shape} is not a valid shape.", file=sys.stderr)
        

# TODO: Step 1 - get height (it must be int!)
def get_height():
    # asks for user input in the height,checks if the height is within range and is a number
    # if it is not a number or is not within in the range, prints an error and prompts user input again
    while True:
        try:
            height = input("Height?: ")
            height = int(height)
            if (0 < height < 80):
                return height
            else:
                print(f"User input: {height} is out of range of 0 < height < 80", file = sys.stderr)
        except:
                print(f"User input: {height} is not a valid height input", file= sys.stderr)
                pass

# TODO: Step 2
def draw_pyramid(height, outline):
    # prints the solid pyramid shape
    if outline == False:
        for counter in range(1, height + 1):
            print((" " * (height - counter) + "*" * (2*counter -1)))
            
    else:
        # prints the outline of the pyramid shape
        for counter in range(1, height + 1):
            if counter == 1:
                print(" " * (height - counter) + "*")
            elif counter == height:
                print("*" * (2 * height - 1))
            else:
                print(" " * (height - counter) + "*" * 1 + " " * (2 * (counter - 1) -1)+ "*" * 1)

# TODO: Step 3
def draw_square(height, outline):
    # prints the solid square shape
    if outline == False:
        for count in range(1, height + 1):
            print("*" * height)
    else:
        # prints the ouline square shape
        for count in range(1, height+1):
            if count == 1:
                print("*" * height)
            elif count == height:
                print("*" * height)
            else:
                print('*' + " "*(height -2) + "*")
    
# TODO: Step 4
def draw_triangle(height, outline):
    # prints the solid triangle shape
    if outline == False:
        for count in range(1, height + 1):
            print("*" * count)

    else:
        # prints the outline triangle shape
        for count in range(1, height + 1):
            if count == 1:
                print("*")
            elif count == height:
                print("*" * height)
            elif count == 2:
                print("*" * count)
            else:
                print("*" + " " * (count - 2) + "*")

def draw_diamond(height, outline):
    # prints the solid diamond shape
    if outline == False:
        top_triangle = math.ceil((height + 1)/ 2)
        for counter in range(1, top_triangle + 1):
            print((" " * (top_triangle - counter) + "*" * (2* counter -1)))

        bottom_triangle = height // 2
        for counter in range(1, bottom_triangle + 1):
            print((" " * counter) + "*" * ((2*(bottom_triangle - counter)) + 1))

    else:
        # prints the outline diamond shape
        top_triangle = round((height + 1)/2)
        for counter in range(1, top_triangle + 1):
            if counter == 1:
                print(" " * (top_triangle - counter) + "*")
            else:
                print(" " * (top_triangle - counter) + "*" * 1 + " " * (2 * (counter - 1) -1)+ "*" * 1)

        bottom_triangle = height // 2
        for counter in range(1, bottom_triangle + 1):
            if counter == height:
                print(" " * counter + "*")

def draw_parallelogram(height, outline):
    # prints the solid parallelogram shape
    if outline == False:
        for count in range(1, height + 1):
            if count == 1:
                print(" " * (height - count) + "*" * height + "*" * (height - count))
            else:
                print(" " * (height - count) + "*" * (count - 1) + "*" * height + "*" * (height - count))
    else:
        # prints the outline parallelogram shape
        for count in range(1, height + 1 ):
            if count == 1:
                print(" " * (height - 1) + "*" * (count - 1) + "*" * height + "*" * (height - count))
            elif count == height:
                print("*" * (2 * count - 1))
            else:
                print(" " * (height - count) + "*" * 1 + " " * ((2 * height -1) - 2) + "*" * 1)

def draw_rectangle(height, outline):
    # prints the solid rectangle shape
    if outline == False:
        for count in range(1, height+1):
            print("*" * (height * 2))
    else: 
        # prints the outline rectangle shape
        for count in range(1, height + 1):
            if (count == height) or (count == 1):
                print("*" * (height * 2))
            else:
                print("*" * 1 +" " * ((height * 2)- 2) + "*") 

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
       draw_pyramid(height, outline)
    if shape == "parallelogram":
        draw_parallelogram(height, outline)
    if shape == "rectangle":
        draw_rectangle(height, outline)
    if shape == "square":
        draw_square(height, outline)
    if shape == "triangle":
        draw_triangle(height, outline)
    if shape == 'diamond':
        draw_diamond(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    while True:
        outline_or_solid = ((input("Outline only: (Y/N) "))).lower()
        if outline_or_solid == 'y':
            outline = True
            return outline
        elif outline_or_solid == 'n':
            outline = False
            return outline
        else:
            print(f"{outline_or_solid} is an invalid response", file=sys.stderr)      

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

