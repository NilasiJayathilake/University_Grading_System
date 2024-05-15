# I declare that my work contains no examples of misconduct, such as plagiarism, or
# collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: W2053081
# Date: 04/12/2023

# This is the staff version
from graphics import *


# outofrange() function uses range function to check whether the entered credits are between 0 and 120 in multiplies
# of 20.
def outofrange(credit):
    if credit not in range(0, 121, 20):
        raise IndexError


# the below variables are used to keep count of each outcome.
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0

# here an empty list called outcome_list is created to store each outcome and corresponding credits as lists.
# outcome_list becomes a nested list. (A list which stores lists as elements)
outcome_list = []

extend = "y"
while extend == "y":
    # Below while loop is used to validate the inputs. Each Input of Credits (Pass credits, Defer Credits,
    # Fail credits) Go through a try and except block. While an error is there the loop will continue to ask the user
    # to enter proper credits for each.
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
            progress_count += 1
            outcome_list.append(["Progress: ", pass_credits, defer_credits, fail_credits])
        elif pass_credits == 100:
            outcome = "Progress(Module Trailer)"
            trailer_count += 1
            outcome_list.append(["Progress(Module Trailer) : ", pass_credits, defer_credits, fail_credits])
        elif (pass_credits + defer_credits) >= fail_credits:
            outcome = "Do not Progress ( Module Retriever)"
            retriever_count += 1
            outcome_list.append(["Module Retriever: ", pass_credits, defer_credits, fail_credits])
        elif fail_credits == 80 or 100 or 120:
            outcome = "Exclude"
            excluded_count += 1
            outcome_list.append(["Excluded: ", pass_credits, defer_credits, fail_credits])
        print("Progression Outcome: ", outcome)
    extend = input(
        "Would you like to enter a another set of data?\nType y to continue \nType q to quit \n").lower()
    if extend != "q":
        continue
    else:
        total_outcomes = progress_count + trailer_count + retriever_count + excluded_count
        print('─' * 10)


        # The function outcome_printer() is used for part 2 and 3.
        # A For loop is used to iterate through every element of 'outcome_list' Nested List.
        # A Formatted String (f String) is used to print the desired outcome.
        def outcome_printer():
            f = open("text.txt", "w")
            print("Part 2")
            for y in outcome_list:
                print("{}{}".format(y[0], ", ".join(map(str, y[1:]))))
                f.writelines(f"{y[0]}{','.join(map(str, y[1:]))}\n")

            f.close()
            f = open("text.txt", "r")
            print('─' * 10)
            print("Part 3")
            for line in f:
                print(line.strip())
            f.close()


        outcome_printer()
        break


# When the staff enters q the graph() function is activated. Which will generate the graph accordingly
def graph():
    # creating the window
    win = GraphWin("Histogram ", 600, 600)
    win.setBackground("mint cream")
    # Title Properties
    title = Text(Point(200, 30), "Histogram Results")
    title.setStyle("bold")
    title.setSize(14)
    title.setFill("black")
    title.draw(win)
    # creating a horizontal line
    hor_Line = Line(Point(100, 500), Point(500, 500))
    hor_Line.draw(win)
    # creating the bar graphs. Rectangles are used as bar graphs.
    # A bar for each outcome will only be displayed if the count is more than 0.
    # The count of each outcome is passed to a point of the rectangle's left corner point y index
    if progress_count > 0:
        progress = Rectangle(Point(120, 500 - (progress_count * 70)), Point(200, 500))
        progress.setFill("light pink")
        progress.draw(win)
        pcText = Text(Point(150, 500 - (progress_count * 70) - 20), progress_count)
        pcText.setFill("dark grey")
        pcText.setStyle("bold")
        pcText.draw(win)

    if trailer_count > 0:
        trailer = Rectangle(Point(220, 500 - (trailer_count * 70)), Point(300, 500))
        trailer.setFill("dark red")
        trailer.draw(win)
        tcText = Text(Point(250, 500 - (trailer_count * 70) - 20), trailer_count)
        tcText.setFill("dark grey")
        tcText.setStyle("bold")
        tcText.draw(win)

    if retriever_count > 0:
        retriever = Rectangle(Point(320, 500 - (retriever_count * 70)), Point(400, 500))
        retriever.setFill("light green")
        retriever.draw(win)
        rcText = Text(Point(350, 500 - (retriever_count * 70) - 20), retriever_count)
        rcText.setFill("dark grey")
        rcText.setStyle("bold")
        rcText.draw(win)

    if excluded_count > 0:
        excluded = Rectangle(Point(420, 500 - (excluded_count * 70)), Point(500, 500))
        excluded.setFill("sky blue")
        excluded.draw(win)
        ecText = Text(Point(450, 500 - (excluded_count * 70) - 20), excluded_count)
        ecText.setFill("dark grey")
        ecText.setStyle("bold")
        ecText.draw(win)

    # subtitles to label each bar graph is created below
    subTitle1 = Text(Point(150, 520), "Progress")
    subTitle2 = Text(Point(250, 520), "Trailer")
    subTitle3 = Text(Point(350, 520), "Retriever")
    subTitle4 = Text(Point(450, 520), "Excluded")

    subTitle1.setStyle("bold")
    subTitle2.setStyle("bold")
    subTitle3.setStyle("bold")
    subTitle4.setStyle("bold")

    subTitle1.setFill("dark grey")
    subTitle2.setFill("dark grey")
    subTitle3.setFill("dark grey")
    subTitle4.setFill("dark grey")

    subTitle1.draw(win)
    subTitle2.draw(win)
    subTitle3.draw(win)
    subTitle4.draw(win)

    # displaying total outcomes
    outcome_title = Text(Point(100, 570), str(total_outcomes))
    outcome_title.setStyle("bold")
    outcome_title.setFill("dark grey")
    outcome_title.draw(win)
    subTitle5 = Text(Point(180, 570), "  Outcomes in Total")
    subTitle5.setStyle("bold")
    subTitle5.setFill("dark grey")
    subTitle5.draw(win)
    win.mainloop()


graph()

'''
References

Python, R. (2023). Python ‘while’ Loops (Indefinite Iteration) – Real Python. [online] realpython.com. 
Available at: https://realpython.com/python-while-loop/ [Accessed 23 Nov. 2023].

stackoverflow (2011). Printing a list of lists, without brackets. [online] Stack Overflow.
 Available at: https://stackoverflow.com/questions/8370966/printing-a-list-of-lists-without-brackets [Accessed 28 Nov. 2023].
 
 W3Schools (2023). Python range() Function. [online] www.w3schools.com. 
 Available at: https://www.w3schools.com/python/ref_func_range.asp [Accessed 28 Nov. 2023].
 
 Yadav, P. (2022). List Input In Python. [online] Scaler Topics. 
 Available at: https://www.scaler.com/topics/list-input-in-python/ [Accessed 27 Nov. 2023].

'''
