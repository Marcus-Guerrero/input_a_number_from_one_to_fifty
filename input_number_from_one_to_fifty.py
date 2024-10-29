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

result_1= []
result_2= []
result_3= []
result_4= []
result_5= []

for val in value_archive:
    if 1<= val <=10:
        result_1.append(val)
    elif 11<= val <= 20:
        result_2.append(val)
    elif 21<= val <= 30:
        result_3.append(val)
    elif 31<= val <= 40:
        result_4.append(val)
    else:
        result_5.append(val)

val_1=(len(result_1))
val_2=(len(result_2))
val_3=(len(result_3))
val_4=(len(result_4))
val_5=(len(result_5))

print (f" 1-10: {val_1} \n 11-20: {val_2} \n 21-30: {val_3} \n 31-40: {val_4} \n 41-50: {val_5}")


#Print all the values inputted by arrange in various ranges from 1-10...all the way to 41-50

