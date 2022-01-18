#Python Dates
import  datetime
import time

x = datetime.datetime.now()
print(x)
print(x.day,x.month,x.year)
print(x.strftime('%a'),'||',x.strftime('%A'))
print(x.strftime('%b'),'||',x.strftime('%B'))
print(x.strftime('%H'),'||',x.strftime('%I'))

#a. Find no of Days between two dates / datetime
d0 = datetime.date(x.year,x.month,x.day)
d1 = datetime.date(2021,11,22)
delta = d0 - d1
print('days : ',delta.days)

#Find Day of the date / datetime
print('Day of the date :',x.strftime('%a'),'||',x.strftime('%A'))

#Find month of the date / datetime
print('Month of the date :',x.strftime('%b'),'||',x.strftime('%B'))

#Find year of the date
print('Year of the date',x.year)

#Convert string to date / datetime
my_time = time.strptime('Nov 24 2021  3:00PM', '%b %d %Y %I:%M%p')
print(my_time)

#Subtract n no of days from a date and find that date
def FindDate(n):
    return datetime.datetime.now() - datetime.timedelta(n);

print('Subtract n no of days :',FindDate(23))

#Add year to a date
def AddYear(numofyear):
    dateObject = datetime.datetime.now();
    endDate = dateObject.replace(year=dateObject.year + numofyear);
    return  endDate;

print('Added year to a date :',AddYear(2))

#Find date of next Tuesday or Wednesday
def FindNextDay(weekday):
    d = datetime.datetime.now();
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

print('date of next Tuesday :',FindNextDay(1),'||','date of next Wednesday :',FindNextDay(2))

#Add month to a date
def AddMonth(n):
    dateObject = datetime.datetime.now();
    endDate = dateObject.replace(month=dateObject.month + n);
    return  endDate;
print('Added month to a date :',AddMonth(1))

#Find no of months between two dates / datetime
d0 = datetime.date(x.year,x.month,x.day);
d1 = datetime.date(2019,1,22);
delta = d0.month - d1.month;
print('No of months between two dates :',delta)

#Find no of years between two dates / datetime
delta = d0.year - d1.year;
print('No of years between two dates :',delta)