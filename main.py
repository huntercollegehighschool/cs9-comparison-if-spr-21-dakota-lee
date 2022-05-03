program = input("Which part(1, 2, 3, 4, or 5)? ")

while program not in ['1', '2', '3', '4', '5']:
  print("Enter a valid part of the assignment.")
  program = input("Which part(1, 2, 3, 4, or 5)? ")
  
if program == '1':
  import part1
  
elif program == '2':
  import part2
  
elif program == '3':
  import part3
  
elif program == '4':
  import part4
  
elif program == '5':
  import part5
