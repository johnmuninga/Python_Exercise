#this function validate the id number based on the Luhn algorithm
def validate_id(id_number):
    if len(id_number) != 13:
        return False

    sum_even = 0
    sum_odd = 0
    for i, digit in enumerate(id_number[:12]):
        digit = int(digit)
        if i % 2 == 0:
            sum_odd += digit
        else:
            doubled_digit = digit * 2
            if doubled_digit > 9:
                doubled_digit -= 9
            sum_even += doubled_digit

    total_sum = sum_odd + sum_even
    check_digit = 10 - (total_sum % 10)
    if check_digit == 10:
        check_digit = 0

    return check_digit == int(id_number[12])


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
if validate_id(id_number):
    decode_id(id_number)
else:
    print("Invalid ID number.\n")
