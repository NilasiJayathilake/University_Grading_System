# I declare that my work contains no examples of misconduct, such as plagiarism, or
# collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: W2053081
# Date: 04/12/2023

# This is the student version
def outofrange(credit):
    if credit not in range(0, 121, 20):
        raise IndexError


while True:
    while True:
        try:
            pass_credits = int(input("Please Enter your Pass Credits: "))
            outofrange(pass_credits)
            break
        except ValueError:
            print("Integer required")
        except IndexError:
            print("Out of range")

    while True:
        try:
            defer_credits = int(input("Please Enter your Defer Credits: "))
            outofrange(defer_credits)
            break
        except ValueError:
            print("Integer required")
        except IndexError:
            print("Out of range")

    while True:
        try:
            fail_credits = int(input("Please Enter your Fail Credits: "))
            outofrange(fail_credits)
            break
        except ValueError:
            print("Integer required")
        except IndexError:
            print("Out of range")
    outcome = " "
    total = pass_credits + defer_credits + fail_credits
    # checking whether the credit total is 120 or not
    if total != 120:
        print("Total Credits Incorrect")
    # Count of each variable is incremented everytime that outcome is output.
    # Using the .append() function elements are added to the "outcome_list"
    else:
        if pass_credits == 120:
            outcome = "Progress"
        elif pass_credits == 100:
            outcome = "Progress(Module Trailer)"
        elif (pass_credits + defer_credits) >= fail_credits:
            outcome = "Do not Progress ( Module Retriever)"
        elif fail_credits == 80 or 100 or 120:
            outcome = "Exclude"
        print("Progression Outcome: ", outcome)
    break


