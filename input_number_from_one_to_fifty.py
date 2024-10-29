#State a list
value_archive= []

#Place a while loop
while True:

    #Place another while loop for the input and conditions
    try:
        while True:
            #Create a statement that ask users to input a number from 1-50
            range_values=int(input("Enter any number from 1-50: "))

            #State conditions wherein a user can only put numbers from 1-50
            if 1<= range_values <= 50:
                print ("Please enter another number another number if you want to continue, if not, input an invalid number, thank you!")
            elif str(range_values):
                print("Wrong")
            else:
                break

            # Store the values to the general list
            value_archive.append(range_values)

        break  # Breaking the final loop

    except:
        print ("Please input a number only")


#Place five list for storing designated values stated in the conditions
result_1= []
result_2= []
result_3= []
result_4= []
result_5= []

for val in value_archive: # State the conditions for sorting the values in different list
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

#Place them in five different variables for organization
val_1=(len(result_1))
val_2=(len(result_2))
val_3=(len(result_3))
val_4=(len(result_4))
val_5=(len(result_5))

#Print all the values inputted by arrange in various ranges from 1-10...all the way to 41-50
print (f" 1-10: {val_1} \n 11-20: {val_2} \n 21-30: {val_3} \n 31-40: {val_4} \n 41-50: {val_5}")




