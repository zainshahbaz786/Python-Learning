import datetime
# for the functionalities via using the date
d = datetime.datetime.now()
print("Right Now, the date is: {0} {1} {2}.".format((d.strftime("%d")), (d.strftime("%b")), (d.strftime("%Y"))))
print("Time is About: {0}: {1} {2}.".format((d.strftime("%I")), (d.strftime("%M")), (d.strftime("%p"))))
