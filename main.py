import django_setup
from action_over_models import (
    add_subject, edit_subject, delete_subject,
    add_teacher,add_class, edit_class, delete_class,
    add_student, add_schedule, add_grade
)

def main():
    while True:
        print("1. Add Subject")
        print("2. Edit Subject")
        print("3. Delete Subject")
        print("4. Add Teacher")
        print("5. Add Class")
        print("6. Edit Class")
        print("7. Delete Class")
        print("8. Add Student")
        print("9. Add Schedule")
        print("10. Add Grade")
        print("11. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_subject()
        elif choice == 2:
            edit_subject()
        elif choice == 3:
            delete_subject()
        elif choice == 4:
            add_teacher()
        elif choice == 5:
            add_class()
        elif choice == 6:
            edit_class()
        elif choice == 7:
            delete_class()
        elif choice == 8:
            add_student()
        elif choice == 9:
            add_schedule()
        elif choice == 10:
            add_grade()
        elif choice == 11:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


