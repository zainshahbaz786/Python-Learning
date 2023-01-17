import json
# json data:
x = {"name": "zain", "degree": "BSCS", "gpa": 2.85, "batch": "18-22"}
y=json.dumps(x,indent=6)
print("From Python to JSON is by using dumps: ",y)

z=json.loads(y)
print("Now from JSON to Python: ", z)
# reading a file from the external storage
with open('sample2.json') as Sample_File:
    data=json.load(Sample_File)
print('\n\n Printing in Simple JSON Format: \n', data)
Python_Data=json.dumps(data, indent=5)
print(Python_Data)

#here, I am reading external JSON file then displaying it and then converting it to Python Dictionary
