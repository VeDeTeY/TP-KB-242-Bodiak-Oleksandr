import csv
from Student import Student

class File:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, students):
        if not students:
            return
        
        data = []
        for student in students:
            data.append({
                'name': student.name,
                'phone': student.phone,
                'email': student.email,
                'group': student.group
            })
        
        with open(self.filename, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'email', 'group'])
            writer.writeheader()
            writer.writerows(data)
    
    def read(self):
        students = []
        try:
            with open(self.filename, "r", encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    student = Student(row['name'], row['phone'], row['email'], row['group'])
                    students.append(student)
        except FileNotFoundError:
            print(f"Файл {self.filename} не знайдено. Створено пустий список.")
        except Exception as e:
            print(f"Помилка при зчитуванні файлу: {e}")
        
        return students