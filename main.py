def turnaround():

# user input
  userwords = input('Please enter a phrase here')

# split up the string
  splitup = userwords.split()

# turn around the order
  mixup = splitup[::-1]

# and put it back together
  putback = "**".join(mixup)

# print to screen
  print(putback)

turnaround()
