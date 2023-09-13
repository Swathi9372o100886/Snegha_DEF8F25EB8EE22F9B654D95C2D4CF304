#Leap year

"""
year % 4==0&
year% 100! =0/
year%400=0

"""
def isLeapYear(year):
  if(year% 4==0):
    return True
  else:
    return False
    
year=2017
if isLeapYear(year):
  print('{} is a leapyear.'.format)
else:
     print('{} is not a leap year.'.format(year))