"""
    Mr.Jochen working on creating application for his school. Here are the following
    functions that he would to like create -
        1. get_student_marks - which takes student mark1, mark2 and mark3
        and return its total.
        2. get_student_grade - which calls get_student_marks and returns “A”
        grade if mark1 is greater than 50, else it should return grade “B”.
        3. validate_marks - which validates mark1, mark2, mark3. Here are the
        validations -
            1. If any of the mark is less than zero or not a number, this function
            should return False.
            2. If any of the mark is greater than 25, then this function should
            return False.
            3. Else, this function should return True
        4. validate_student_name - this function should check whether student
        name is of length > 5 and less than 25. If name valid, return True, else return False
        5. main - Function which should take name and marks (m1, m2, m3
        respectively).
            a. Call validate_student_name function if it gives False, print “Invalid
            Student Name”.
            b. If not, Call validate_marks function and if it gives False, print
            “Invalid Mark input”.
            c. If not, do a simple check, ensure minimum score of each marks
            (m1, m2, m3) is greater than or equal to 7. If not, print “You got failed, grades
            cannot be calculated”.
            d. If not, call get_student_grade method and print the grade which this
            function returned as the output.
"""
def get_student_marks(mark1,mark2,mark3):
    return mark1+mark2+mark3

def get_student_grade():
    total = int(get_student_marks(mark1,mark2,mark3))
    if(total>=50):
        return "A"
    else:
        return "B"

def validate_marks(mark1,mark2,mark3):
    if(mark1<0 or mark2<0 or mark3<0 ):
        if(mark1<25 or mark2<25 or mark3<25):
            return False
    else:
        return True

def validate_student_name(Stud_name):
    if(5<len(Stud_name)<=25):
        return True
    else:
        return False

def main(Stud_name,mark1,mark2,mark3):

    name_check = validate_student_name(Stud_name)
    if(name_check == False):
        print("Invalid Student Name")
    elif(validate_marks(mark1,mark2,mark3) == False):
        print("Invalid Mark input")
    elif(min(mark1,mark2,mark3)<7):
        print("You got failed, grades cannot be calculated")
    else:
        grade = get_student_grade()
        return grade

Stud_name = input("Name: ")
mark1 = int(input("1st Subject Mark:"))
mark2 = int(input("1st Subject Mark:"))
mark3 = int(input("1st Subject Mark:"))
print("Grade: ",main(Stud_name,mark1,mark2,mark3))