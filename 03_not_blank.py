# function goes here

# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("sorry this cant be blank. Please reattempt")
        else:
            return response



# main routine goes here
while True:
    name = not_blank("Enter your name(or 'xxx' to quit ")
    if name == "xxx":
        break


print("we are done")
