def decode_id(id_number):
    #Extract information from the ID number
    birth_date = id_number[:6]
    gender_code = int(id_number[6:10])
    citizenship_code = int(id_number[10])

    #Formatting to get the date of birth
    year = birth_date[:2]
    month = birth_date[2:4]
    day = birth_date[4:]
    date_of_birth = f"{day}/{month}/{year}"

    #Declaring if statement to get the gender
    if gender_code >= 5000:
        gender = "male"
    else:
        gender = "female"

    #Declaring if statement to get the citizenship status
    if citizenship_code == 0:
        citizenship ="a South African citizen"
    else:
        citizenship ="a permanent resident"

    #Displaying The individual information
    print(f"Your date of birth is {date_of_birth}.")
    print(f"You are {gender}.")
    print(f"You are {citizenship}.")


#prompting the user to insert their ID number
id_number = input("Please enter your ID number:\n")
decode_id(id_number)
