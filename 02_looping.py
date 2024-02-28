# main routine starts here

# set maximum number of tickets below
MAX_TICKETS: int = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit")

    if name == 'xxx':
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s "
          "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
