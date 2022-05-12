'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below

month = input("Enter the name of a month: ")
month = month.capitalize()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if month not in months:
  print("not a month :(")
  exit()
  
monthNum = months.index(month)

daysPerMonth = [31, "28 or 29", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
numOfDays = daysPerMonth[int(monthNum)]

print(str(numOfDays))


'''
using four blocks of code; it doesn't look so nice to look at so i made the thing above (especially since i dont know if you can combine the ors or not or if i forgot how to hah)

if month == months[0] or month == months[2] or month == months[4] or month == months[6] or month == months[7] or month == months[9] or month == months[11]:
  print("31")
elif month == months[3] or month == months[5] or month == months[8] or months == months[10]:
  print("30")
elif month == months[1]:
  print("28 or 29")
else:
  print("thats not a month :(")
'''

