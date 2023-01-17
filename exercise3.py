#printing multiples of 3 using generators
print("printing....")
def Table_Generator_Function(n):
    for i in range(1,11):
        yield (n*i)
       
        
def Table_Printer():        
    num=int(input("Enter the Table Number: ")) 
    x=Table_Generator_Function(num)
    for value in Table_Generator_Function(num):
        print(value)
        
Table_Printer()