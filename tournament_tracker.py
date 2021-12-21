# welcome user to tournament and prompt for number of particints, N
# initialize a list of length N and values set to None
# begin while loop: present menu and prompt user for option
    # if user chooses register
        # prompt user for slot and name until valid entry (while loop)
        # update list with name at chosen slot
    # if user chooses cancel
        # prompt user for slot and name until valid entry (while loop)
    # if user chooses view
        # prompt user for valid selected slot (while loop)
        # print list for indices 5 below selected through 5 above selected
    # if user chooses save
        # prompt user to confirm changes in csv (while loop)
        # save changes
    # if user chooses exit
        # prompt to confirm exit (while loop)
        # exit
        
# Tournament Tracker
# print welcome message
print('Welcome to the Tournaments R Us!')
# prompt for valid n
while True:
    n = input('Enter the number of participants: ')
    try:
        n = int(n)
        break
    except:
        print('Invalid format: Please enter a number.')
# initialize list of n length with None values
roster = [None]*n
# initialize exited boolean for menu while loop
exited = False 
# begin menu prompt while loop 
while exited == False:
    option = input("""
  Participant Menu
====================
1. Sign Up
2. Cancel Sign Up
3. View Participants
4. Save Changes
5. Exit
Please enter the number for the option you want: """)
    # sign up
    if option == '1':
        while True:
            name = input('Participant Name: ')
            desired_slot = input('Desired Starting Slot #[1-{}]: '.format(n))
    # cancel sign up
    elif option == '2':
        continue
    # view participants
    elif option == '3':
        continue
    # save changes
    elif option == '4':
        continue
    # exit
    elif option == '5':
        continue
    # invalid entry
    else:
        print("Inalid entry. Please enter a value 1 - 5.")
