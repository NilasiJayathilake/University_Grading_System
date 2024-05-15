# I declare that my work contains no examples of misconduct, such as plagiarism, or
# collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: W2053081
# Date: 04/12/2023

print("Hello! Welcome to the University Grading System")
version = int(input("If you are a Student enter 1 to continue \nIf you are a Staff enter 2 to continue \nEnter 3 "
                    "to exit\n"))
if version == 1:
    import W2053081_student
elif version == 2:
    import W2053081_staff
else:
    print("Thank You!")