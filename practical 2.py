#Functions
def ticketNotSold():
    global totalVisited
    totalVisited += 1

def ticketSold():
    global totalVisited, totalAmnt
    totalVisited += 1
    totalAmnt += 5

def displayTotals():
    print("Total People Visited: ",totalVisited)
    print("Total Amount Collected: ", totalAmnt)

def displayTicketSold():
    print("Total Number of Ticket Sold: ",totalAmnt//5)

#Main Program
totalVisited = 0
totalAmnt = 0
print("TICKET SELLING BOOTH")
while True:
    print('''
Please Enter Action Corresponding Code
0: To Exit
1: Reports
2: People Visited but Ticket Not Sold
3: People Visited and Ticket Also Sold
4: Display Total People and Total Amount Collected
5: Display number of tickets sold''')
    code = int(input("--> "))
    if code == 0:
        print("Exiting")
        break
    elif code == 1:
        displayTotals()
        displayTicketSold()
    elif code == 2:ticketNotSold()
    elif code == 3:ticketSold()
    elif code == 4:displayTotals()
    elif code == 5:displayTicketSold()
    else: print("Please Enter a correct code from given options")

print("Thank you for using our services")
