#State a list
value_archive={}

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

    value_archive={
        "coded_value": range_values
    }

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

one_to_ten_values = []
eleven_to_twenty = []
twenty_one_to_thirty = []
thirty_one_to_forty = []
forty_one_to_fifty = []

for value, digit in value_archive.items():
    if 1<= digit <= 10:
        one_to_ten_values.append(digit)
        one_to_ten_values = [digit]
    elif 11<= digit <= 20:
        eleven_to_twenty.append(digit)
        eleven_to_twenty = [digit]
    elif 21<= digit <= 30:
        twenty_one_to_thirty.append(digit)
        twenty_one_to_thirty = [digit]
    elif 31<= digit <= 40:
        thirty_one_to_forty.append(digit)
    elif 41<= digit <= 50:
        forty_one_to_fifty.append(digit)
        forty_one_to_fifty = [digit]

print (one_to_ten_values)


#Print all the values inputted by arrange in various ranges from 1-10...all the way to 41-50

#range_1= one_to_ten_values.count(range_values)
#range_2= eleven_to_twenty.count(range_values)
#range_3= twenty_one_to_thirty.count(range_values)
#range_4= thirty_one_to_forty.count(range_values)
#range_5= forty_one_to_fifty.count(range_values)
