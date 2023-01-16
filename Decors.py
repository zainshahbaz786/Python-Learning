# Logic that add full stop where it finds double space USING Decorators
def correction(line):
    print(" Using Decors, replacing double space with Full Stop")
    if "  " in line:
        new_line = line.replace("  ", ".")
        print(new_line)


#correction("My name is Zain  I am Software Engineer")
