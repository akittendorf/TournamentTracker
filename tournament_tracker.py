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
# import csv
import csv
# print welcome message
print('Welcome to the Tournaments R Us!')
# prompt for valid n
while True:
    n = input('Enter the number of participants: ')
    try:
        n = int(n)
        # exit while loop
        break
    except:
        print('Invalid format: Please enter a number.')
# initialize list of n+1 length with None values to account for non-0 indexing
roster = [None]*(n+1)
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
            # get name and starting slot
            name = input('Participant Name: ').lower()
            desired_slot = input('Desired Starting Slot #[1-{}]: '.format(n))
            # check valid entry
            try:
                desired_slot = int(desired_slot)
                # if slot is empty
                if roster[desired_slot] == None and desired_slot < (n + 1) and desired_slot != 0:
                    # fill slot with given name
                    roster[int(desired_slot)] = name
                    # print success message
                    print('Success:\n{} is signed up in starting slot {}.'.format(name, desired_slot))
                    # exit while loop
                    break
                elif roster[desired_slot] != None:
                    print('Error:')
                    print('Slot #{} is filled. Please try again.'.format(desired_slot))
                else:
                    print('Invalid entry. Desired Starting Slot must be a number between 1 and {}.'.format(n))
            # for slots that aren't integers or are greater > len(roster)
            except:
                print('Invalid entry. Desired Starting Slot must be a number between 1 and {}.'.format(n))
    # cancel sign up
    elif option == '2':
        while True:
            # get name and starting slot
            name = input('Participant Name: ').lower()
            slot = input('Starting Slot #[1-{}]: '.format(n))
            try:
                slot = int(slot)
                # valid entry
                if roster[slot] == name:
                    # overwrite entry name as None
                    roster[slot] = None
                    # print success message
                    print('Success:\n{} has been cancelled from starting slot #{}'.format(name,slot))
                    # exit while loop
                    break
                elif roster[slot] != name:
                    # print error message
                    print('Error:\n{} is not in that starting slot.'.format(name))
            # for slots that aren't integers
            except:
                print("Invalid entry. That slot doesn't exist. Slot must be a number between 1 and {}.".format(n))
            
    # view participants
    elif option == '3':
        while True:
            # get name and slot
            slot = input('Starting Slot #[1-{}]: '.format(n))
            try:
                slot = int(slot)
                # valid entry
                if slot > 0 and slot < n + 1:
                    print('Starting Slot: Participant')
                    print('Starting Slot #: {}'.format(slot))
                    for i in range(slot - 5, slot + 6):
                        try:
                            if i > 0:
                                print('{}: {}'.format(i, roster[i]))
                        except:
                            continue
                    break
                else:
                    print('Invalid entry. Please enter a number 1 through {}'.format(n))
            except:
                print('Invalid entry. Please enter a number 1 through {}.'.format(n))
        
    # save changes
    elif option == '4':
        while True:
            confirmation = input('Save your changes to CSV? Y/N').lower()
            if  confirmation == 'y':
                with open('roster.csv', 'w') as file:
                    for i in range(1, len(roster)+1):
                        try:
                            file.write('{},{}\n'.format(i, roster[i]))
                        except:
                            continue
                    print('Success:')
                    print('Roster has been saved as roster.csv')
                    break
            elif confirmation == 'n':
                break
            else:
                print('Invalid entry. Please enter "Y" or "N".')
        
    # exit
    elif option == '5':
        print('Exit')
        print('=========')
        print('Any unsaved changes will be lost.')
        while True:
            answer = input('Are you sure you want to exit? Y/N ').lower()
            if answer == 'y':
                print('Okay. Goodbye!')
                quit()
            elif answer == 'n':
                print('Okay. Returning to menu...')
                break
            else:
                print('Invalid entry. Please enter "Y" or "N"')
    # invalid entry
    else:
        print("Inalid entry. Please enter a value 1 - 5.")
