# Codomax AI/ML - Module 2
# Student Grade Calculator


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} mark: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Please enter a mark between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


while True:

    print("\n===== Student Grade Calculator =====")

    name = input("Enter student name: ")

    maths = get_mark("Maths")
    python = get_mark("Python")
    dbms = get_mark("DBMS")
    os = get_mark("Operating Systems")
    ai_ml = get_mark("AI/ML")

    total = maths + python + dbms + os + ai_ml
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    marks = [maths, python, dbms, os, ai_ml]

    if all(mark >= 40 for mark in marks):
        result = "PASS"
    else:
        result = "FAIL"

    print("\n================================")
    print("        STUDENT RESULT")
    print("================================")
    print("Name       :", name)
    print("Maths      :", maths)
    print("Python     :", python)
    print("DBMS       :", dbms)
    print("OS         :", os)
    print("AI/ML      :", ai_ml)
    print("--------------------------------")
    print("Total      :", total)
    print("Percentage :", round(percentage, 2), "%")
    print("Grade      :", grade)
    print("Result     :", result)
    print("================================")

    choice = input(
        "\nDo you want to calculate another student? (yes/no): "
    )

    if choice.lower() != "yes":
        print("Thank you for using Student Grade Calculator!")
        break