import math, time

def print_circle(radius):
    for x in range((2 * radius)+1): 
        for y in range((2 * radius)+1): 
            length = math.sqrt(math.pow((x - radius), 2) + math.pow((y - radius), 2)) 
            if (length > radius - 0.5 and length < radius + 0.5):  
                print("x", end = " ") 
            else: 
                print(" ", end = " ")       
        print() 

def print_triangle(side_length):
    z = side_length - 1
    for x in range(side_length):
        for y in range(z):
            print(end=" ")
        z -= 1
        for i in range(x+1):
            print('x', end = " ")
        print("\r")
          
def print_square(side_length):
    for x in range(side_length):
        for x in range(side_length):
            print('x', end = " ")
        print()
        
while True:
    choice = input("Print circle, triangle, or square?: ")
    if choice.lower() == "circle":
        radius = int(input("What is the radius?: "))
        start = time.time() #could be a better way to calculate time?
        print_circle(radius)
        stop = time.time()
        print("Generated circle with radius", radius, "in", (stop-start), "seconds.")
    elif choice.lower() == "triangle":
        side_length = int(input("What is the length?: "))
        start = time.time()
        print_triangle(side_length)
        stop = time.time()
        print("Generated triangle with length", side_length, "in", (stop-start), "seconds.")
    elif choice.lower() == "square":
        side_length = int(input("What is the length?: "))
        start = time.time()
        print_square(side_length)
        stop = time.time()
        print("Generated square with length", side_length, "in", (stop-start), "seconds.")
    else: print("Invalid input.")