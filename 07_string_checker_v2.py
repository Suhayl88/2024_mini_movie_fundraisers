# checks that users enter a valid response (eg yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)



# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the "
                                       "instructions (y/n): ",
                                       1, yes_no_list)
    print("you chose", want_instructions)

for case in range(0, 5):
    pay_method = string_checker("Choose a payment method (cash / credit):",
                                2, payment_list)

    print("You chose", pay_method)


