#list, dict & set are mutable
rainbow=["violet", "indigo", "blue", "green" ,"yellow", "orange", "red"]
print(rainbow[2])
print("ID of Rainbow before editing is: ", id(rainbow[2]))
rainbow[2]="purple"
print(rainbow)
# as we change the value, it clearly express that list are mutable
print("ID of Rainbow after editing is: ", id(rainbow[2]))

# using tuple and trying to mutate it, even its not pssible
hours=(1,2,3,4,5,6,7,8,9,10,11,12)
print(hours[3])
print(hours)
#hours[3]=15
# if we uncomment above line of code, it wont work
print(hours[3])
print(hours)

