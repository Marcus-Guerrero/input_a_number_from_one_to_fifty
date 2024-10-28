#State a dictionary
values={}

#Place a while loop
while True:

    #Place another while loop for the input and conditions
    while True:
        #Create a statement that ask users to input a number from 1-50
        range_values=int(input("Enter any number from 1-50: "))

        #State conditions wherein a user can only put numbers from 1-50
        if not 1<= range_values <= 50:
            print ("We cannot accept any number that is greater than or less than the range of 1-50, please try again")
        else:
            break #Break the second while loop

#Create another statement that ask users if they want to add more entries, if not, break the first loop
#Print all the values inputted by arrange in various ranges from 1-10...all the way to 41-50

