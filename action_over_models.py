import re
from app_1.models import Class, Student, Schedule, Subject, Teacher, Grade

def add_subject():
    while True:
        name = input("Enter subject name: ").strip()
        if name:
            try:
                Subject.objects.get(name=name)
                print("Subject already exists. Please enter a different subject name.")
            except Subject.DoesNotExist:
                break
        else:
            print("Subject name cannot be empty. Please try again.")
    while True:
        description = input("Enter subject description: ").strip()
        if description:
            break
        print("Subject description cannot be empty. Please try again.")
            
    Subject.objects.create(name=name,description=description)
    print("Subject added successfully.")

def edit_subject():
    while True:
        name = input("Enter the name of the subject you want to edit: ").strip()
        if name:
            try:
                subject = Subject.objects.get(name = name)
                break
            except Subject.DoesNotExist:
                print("Subject does not exist. Please enter a valid subject name.")
        else:
            print("Subject name cannot be empty. Please try again.")
    new_name = input("Enter new subject name (leave blank to keep the current name): ").strip()
    if new_name and not Subject.objects.filter(name=new_name).exists():
        subject.name = new_name

    new_description = input("Enter new subject description (leave blank to keep the current description): ").strip()
    if new_description:
        subject.description = new_description

    subject.save()
    print("Subject updated successfully.")

def delete_subject():
    while True:
        name = input("Enter the name of the subject you want to delete: ").strip()
        if name:
            try:
                subject = Subject.objects.get(name = name)
                subject.delete()
                print("Subject deleted successfully.")
                break
            except Subject.DoesNotExist:
                print("Subject does not exist. Please enter a valid subject name.")
        else:
            print("Subject name cannot be empty. Please try again.")
        
def add_teacher():
    while True:
        first_name = input("Enter teacher's first name: ").strip()
        if first_name:
            break
        print("First name cannot be empty. Please try again.")
       
    while True:
        last_name = input("Enter teacher's last name: ").strip()
        if last_name:
            break
        print("Last name cannot be empty. Please try again.")
        
    while True:
        subject_name = input("Enter subject name: ").strip()
        if subject_name:
            try:
                subject = Subject.objects.get(name = subject_name)
                break
            except Subject.DoesNotExist:
                print("Subject does not exist. Please enter a valid subject name.")
        else:
             print("Subject name cannot be empty. Please try again.")

    Teacher.objects.create(first_name=first_name,last_name=last_name,subject=subject)
    print("Teacher added successfully.")

def add_class():
    while True:
        name = input("Enter class name: ").strip()
        if name:
            try:
                Class.objects.get(name=name)
                print("Class already exists. Please enter a different class name.")
            except Class.DoesNotExist:
                break
        else:
            print("Class name cannot be empty. Please try again.")
    while True:
        year = input("Enter class year: ").strip()
        try:
            year = int(year)
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

    Class.objects.create(name=name,year=year)
    print("Class added successfully.")

def edit_class():
    while True:
        name = input("Enter the name of the class you want to edit: ").strip()
        if name:
            try:
                student_class = Class.objects.get(name = name)
                break
            except Class.DoesNotExist:
                print("Class does not exist. Please enter a valid class name.")
        else:
            print("Class name cannot be empty. Please try again.")

    new_name = input("Enter new class name (leave blank to keep the current name): ").strip()
    if new_name and not Class.objects.filter(name=new_name).exists():
        student_class.name = new_name

    while True:
        new_year = input("Enter new class name (leave blank to keep the current name): ").strip()
        if new_year:
            try:
                student_class.year = int(new_year)
                break
            except ValueError:
                print("Invalid input. Please enter a valid year.")
        else:
            break

    student_class.save()
    print("Class updated successfully.")

def delete_class():
    while True:
        name = input("Enter the name of the class you want to delete: ").strip()
        if name:
            try:
                student_class = Class.objects.get(name = name)
                student_class.delete()
                print("Class deleted successfully.")
                break
            except Class.DoesNotExist:
                print("Class does not exist. Please enter a valid class name.")
        else:
            print("Class name cannot be empty. Please try again.")

def add_student():
    while True:
        first_name = input("Enter student's first name: ").strip()
        if first_name:
            break
        print("First name cannot be empty. Please try again.")
       
    while True:
        last_name = input("Enter student's last name: ").strip()
        if last_name:
            break
        print("Last name cannot be empty. Please try again.")

    while True:
        class_name = input("Enter class name: ").strip()
        if class_name:
            try:
                student_class = Class.objects.get(name=student_class)
                break
            except Class.DoesNotExist:
                print("Class does not exist. Please enter a valid class name.")
        else:
            print("Class name cannot be empty. Please try again.")

    Student.objects.create(first_name=first_name, last_name=last_name, student_class=student_class)
    print("Student added successfully.")

def add_schedule():

    while True:
        subject_name = input("Enter subject name: ").strip()
        if subject_name:
            try:
                subject = Subject.objects.get(name=subject_name)
                break
            except Subject.DoesNotExist:
                    print("Subject does not exist. Please enter a valid subject name.")
        else:
            print("Subject name cannot be empty. Please try again.")
    while True:
        while True:
            teacher_first_name = input("Enter teacher's first name: ").strip()
            if teacher_first_name:
                break
            print("First name cannot be empty. Please try again.")

        while True:
            teacher_last_name = input("Enter teacher's last name: ").strip()
            if teacher_last_name:
                break
            print("Last name cannot be empty. Please try again.")
        
        try:
            teacher = Teacher.objects.get(first_name=teacher_first_name, last_name=teacher_last_name)
            break
        except Teacher.DoesNotExist:
            print("Teacher does not exist. Please enter a valid teacher name.")
        
    while True:
        class_name  = input("Enter class name: ").strip()
        if class_name :
            try:
                student_class = Class.objects.get(name=student_class)
                break
            except Class.DoesNotExist:
                print("Class does not exist. Please enter a valid class name.")
        else:
            print("Class name cannot be empty. Please try again.")

    while True:
        day_of_week = input("Enter day of the week: ").strip()
        if day_of_week:
            break
        print("Day of the week cannot be empty. Please try again.")
    
    while True:
        time = input("Enter start time (HH:MM): ").strip()
        if time:
            break
        print("Start time cannot be empty. Please try again.")
    
    Schedule.objects.create(subject=subject,teacher=teacher,student_class=student_class,day_of_week=day_of_week,time=time)
    print("Schedule added successfully.")
       
def add_grade():
    while True:
        while True:
            student_first_name = input("Enter student's first name: ").strip()
            if student_first_name:
                break
            print("First name cannot be empty. Please try again.")
        
        while True:
            student_last_name = input("Enter student's last name: ").strip()
            if student_last_name:
                break
            print("Last name cannot be empty. Please try again.")
        
        try:
            student = Teacher.objects.get(first_name=student_first_name, last_name= student_last_name)
            break
        except Teacher.DoesNotExist:
            print("Student does not exist. Please enter a valid student name.")

    while True:
        subject_name = input("Enter subject name: ").strip()
        if subject_name:
            try:
                subject = Subject.objects.get(name=subject_name)
                break
            except Subject.DoesNotExist:
                    print("Subject does not exist. Please enter a valid subject name.")
        else:
            print("Subject name cannot be empty. Please try again.")

    while True:
        grade = input("Enter grade: ").strip()
        if grade:
            try:
                grade = int(grade)
                break
            except ValueError:
                print("Invalid input. Please enter a valid grade.")
        else:
            print("Grade cannot be empty. Please try again.")
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if date:
            # Check if date is in the correct format
            if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
                break
            else:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        else:
            print("Date cannot be empty. Please try again.")

    Grade.objects.create(student=student, subject=subject, grade=grade, date=date)
    print("Grade added successfully.")
