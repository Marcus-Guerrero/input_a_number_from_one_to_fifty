#State a list
value_archive= []

#Place a while loop
while True:

    #Place another while loop for the input and conditions
    while True:
        #Create a statement that ask users to input a number from 1-50
        range_values=int(input("Enter any number from 1-50: "))

        #State conditions wherein a user can only put numbers from 1-50
        if 1<= range_values <= 50:
            break  # Break the second while loop
        else:
            print("We cannot accept any number that is greater than or less than the range of 1-50, please try again")

    value_archive.append(range_values)

    while True:
        # Create another statement that ask users if they want to add more entries, if not, break the first loop
        another_entry = input("Would you like to input more numbers (y/n): ")
        if another_entry == "y":
            print("Input another number again")
            break
        elif another_entry == "n":
            break
        elif another_entry != "y" and another_entry != "n":
            print ("Wrong command prompt format, please input (y/n) only")
    if another_entry == "n":
        break

result= len(value_archive)
print (result)
#Print all the values inputted by arrange in various ranges from 1-10...all the way to 41-50

