import Student_list
import Student
import Utils

def main():
    file = Utils.File("lab_3.csv")
    student_list = Student_list.StudentList()
    
    data_from_csv = file.read()
    student_list.students = data_from_csv
    
    def save_data():
        file.write(student_list.students)
        print("Data saved to CSV.")
    
    while True:
        print("\n" + "="*40)
        print("1. Add new student")
        print("2. Delete student")
        print("3. Update student")
        print("4. Show all students")
        print("5. Save data")
        print("6. Exit")
        print("="*40)
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            student_list.addNewElement()
        elif choice == "2":
            student_list.deleteElement()
        elif choice == "3":
            student_list.updateElement()
        elif choice == "4":
            student_list.showAllElements()
        elif choice == "5":
            save_data()
        elif choice == "6":
            print("Saving data...")
            save_data()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()