#program to display calender of the given month and Year

#import calender module
import calendar


#yy = 2023 # year
#mm = 11 # month

#testcommit
#input the month and year from user
yy = int(input("Enter year:"))
mm = int(input("Enter Month:"))

#Disply the calender

#print(yy, mm)
print(calendar.month(yy, mm))
