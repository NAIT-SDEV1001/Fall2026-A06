concert_name = input("What is the name of the concert tonight? ")
has_ticket = input("Do you have a ticket? (y/n) ")
if has_ticket == 'y':
    ticket_type = input("What type of ticket do you have? (VIP or Standard) ")

if not has_ticket == "y":
    print("Sorry you need a ticket to get in")
elif concert_name == "taylor swift" and ticket_type == "VIP":
    print("you're in the right place")
    print("have fun superstar!")
elif concert_name == "taylor swift" and ticket_type == "Standard":
    print("enjoy the show")
elif concert_name == "billie eilish":
    print("this concert is next door")
else:
    print("this is not the concert you are looking for")


