import Generators
import Decors
import Comprehension
# Python Basics Practice
# declaring variables,  list
Fn, Ln = "Zayn" , "Shahbaz."
Name = Fn + " " + Ln
x = float(12.0)
y = float(9.0)
z = x+y
myStacks = ["React JS", "Angular JS", "Next JS", "TailwindCSS"]

# calling a function

def intro():

    print("Greetings Everyone,\n Myself, ", Name, "My Age is ", z, "\n")
    print("My Working Stacks are: ")
    for i in range(0, 4):
        print(myStacks[i])

    print("There are few more stacks in which i worked deeply but, here I just mentioned:"+str(len(myStacks)))
    print("Stacks are printed in List because we learn, grow and enhance in new stacks.")

# Main Code Region


intro()
print("Now I am using Generators to print Table.")
Generators.Table_Printer()
Decors.correction("My name is Zain  I am a Software Engineer by profession")
Comprehension.showing_comprehension()




















