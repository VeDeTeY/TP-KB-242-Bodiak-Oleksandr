from Student import Student

class StudentList:
    
    def __init__(self):
        self.students = []
    
    def addNewElement(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        email = input("Please enter student email: ")
        group = input("Please enter student group: ")
        
        new_student = Student(name, phone, email, group)
        
        insertPosition = 0
        for student in self.students:
            if name > student.name:
                insertPosition += 1
            else:
                break
        
        self.students.insert(insertPosition, new_student)
        print("New element has been added")
        return
    
    def deleteElement(self):
        name = input("Please enter name to be deleted: ")
        deletePosition = -1
        
        for item in self.students:
            if name == item.name:
                deletePosition = self.students.index(item)
                break
        
        if deletePosition == -1:
            print("Element was not found")
        else:
            print("Delete position " + str(deletePosition))
            del self.students[deletePosition]
        return
    
    def updateElement(self):
        name = input("Please enter name to be updated: ")
        deletePosition = -1
        
        for item in self.students:
            if name == item.name:
                deletePosition = self.students.index(item)
                break
        
        if deletePosition == -1:
            print("Element was not found")
        else:
            del self.students[deletePosition]
            
            name = input("Please enter student name: ")
            phone = input("Please enter student phone: ")
            email = input("Please enter student email: ")
            group = input("Please enter student group: ")
            
            new_student = Student(name, phone, email, group)
            
            insertPosition = 0
            for student in self.students:
                if name > student.name:
                    insertPosition += 1
                else:
                    break
            
            self.students.insert(insertPosition, new_student)
            print("Element has been updated")
        return
    
    def showAllElements(self):
        for item in self.students:
            print("Name: " + item.name + ", Phone: " + item.phone + ", Email: " + item.email + ", Group: " + item.group)
        return