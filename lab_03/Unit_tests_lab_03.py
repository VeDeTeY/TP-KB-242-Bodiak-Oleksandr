import unittest
import os
from unittest.mock import patch
from io import StringIO
from Student import Student
from Student_list import StudentList
from Utils import File


class TestStudentList(unittest.TestCase):
    
    def setUp(self):
        self.student_list = StudentList()
        
        self.student_list.students = [
            Student("Andriy", "+380501111111", "andriy@gmail.com", "КБ-242"),
            Student("Maria", "+380502222222", "maria@gmail.com", "КБ-242")
        ]
    
    def test_addNewElement(self):
        """Тест додавання нового елементу"""
        initial_count = len(self.student_list.students)
        
        with patch("builtins.input", side_effect=["Oleg", "+380503333333", "oleg@gmail.com", "КБ-242"]):
            self.student_list.addNewElement()
        
        self.assertEqual(len(self.student_list.students), initial_count + 1)
        names = [s.name for s in self.student_list.students]
        self.assertIn("Oleg", names)
        
        ############## Перевірка сортування ##############
        self.assertTrue(names.index("Andriy") < names.index("Maria") < names.index("Oleg"))
    
    def test_deleteElement_found(self):
        """Тест видалення існуючого елемента"""
        initial_count = len(self.student_list.students)
        
        with patch("builtins.input", return_value="Andriy"):
            self.student_list.deleteElement()
        
        self.assertEqual(len(self.student_list.students), initial_count - 1)
        names = [s.name for s in self.student_list.students]
        self.assertNotIn("Andriy", names)
    
    def test_deleteElement_not_found(self):
        """Тест видалення неіснуючого елемента"""
        initial_count = len(self.student_list.students)
        
        with patch("builtins.input", return_value="NonExistent"):
            self.student_list.deleteElement()
        
        self.assertEqual(len(self.student_list.students), initial_count)
    
    def test_updateElement_found_and_resorted(self):
        """Тест оновлення елемента з пересортуванням"""
        with patch("builtins.input", side_effect=["Andriy", "Aaron", "+380509999999", "aaron@gmail.com", "КБ-245"]):
            self.student_list.updateElement()
        
        names = [s.name for s in self.student_list.students]
        self.assertIn("Aaron", names)
        self.assertNotIn("Andriy", names)
        
        ################ Перевірка сортування після оновлення ################
        self.assertEqual(names[0], "Aaron")
        self.assertEqual(names[1], "Maria")
        
        updated_student = self.student_list.students[0]
        self.assertEqual(updated_student.phone, "+380509999999")
        self.assertEqual(updated_student.email, "aaron@gmail.com")
        self.assertEqual(updated_student.group, "КБ-245")
    
    def test_updateElement_not_found(self):
        """Тест оновлення неіснуючого елемента"""
        initial_count = len(self.student_list.students)
        
        with patch("builtins.input", return_value="NonExistent"):
            self.student_list.updateElement()
        
        self.assertEqual(len(self.student_list.students), initial_count)
    
    def test_showAllElements(self):
        """Тест виведення всіх елементів"""
        with patch("sys.stdout", new_callable=StringIO) as fake_output:
            self.student_list.showAllElements()
            output = fake_output.getvalue()
        
        self.assertIn("Andriy", output)
        self.assertIn("+380501111111", output)
        self.assertIn("andriy@gmail.com", output)
        self.assertIn("КБ-241", output)


class TestFileHandler(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_students.csv"
        self.csv_handler = File(self.test_file)
        
        self.students = [
            Student("Ivan", "+380501234567", "ivan@gmail.com", "КБ-241"),
            Student("Maria", "+380509876543", "maria@gmail.com", "КБ-242")
        ]
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_write(self):
        """Тест запису у файл"""
        self.csv_handler.write(self.students)
        self.assertTrue(os.path.exists(self.test_file))
    
    def test_write_empty_list(self):
        """Тест запису порожнього списку"""
        self.csv_handler.write([])
        ################ Файл не повинен створюватися для порожнього списку ##################
        self.assertFalse(os.path.exists(self.test_file))
    
    def test_read_write_cycle(self):
        """Тест циклу запис-читання"""
        self.csv_handler.write(self.students)
        read_students = self.csv_handler.read()
        
        self.assertEqual(len(read_students), len(self.students))
        
        ################ Перевірка всіх полів ################
        for i in range(len(self.students)):
            self.assertEqual(read_students[i].name, self.students[i].name)
            self.assertEqual(read_students[i].phone, self.students[i].phone)
            self.assertEqual(read_students[i].email, self.students[i].email)
            self.assertEqual(read_students[i].group, self.students[i].group)
            self.assertIsInstance(read_students[i], Student)
    
    def test_read_nonexistent_file(self):
        """Тест читання неіснуючого файлу"""
        non_existent_file = File("non_existent_file.csv")
        students = non_existent_file.read()
        
        self.assertEqual(len(students), 0)


class TestStudent(unittest.TestCase):
    
    def setUp(self):
        self.student = Student("Alice", "+380501234567", "alice@gmail.com", "КБ-242")
    
    def test_student_creation(self):
        """Тест створення студента"""
        self.assertEqual(self.student.name, "Alice")
        self.assertEqual(self.student.phone, "+380501234567")
        self.assertEqual(self.student.email, "alice@gmail.com")
        self.assertEqual(self.student.group, "КБ-242")
    
    def test_student_properties_setter(self):
        """Тест встановлення властивостей через setter"""
        self.student.name = "Bob"
        self.student.phone = "+380509999999"
        self.student.email = "bob@gmail.com"
        self.student.group = "КБ-241"
        
        self.assertEqual(self.student.name, "Bob")
        self.assertEqual(self.student.phone, "+380509999999")
        self.assertEqual(self.student.email, "bob@gmail.com")
        self.assertEqual(self.student.group, "КБ-241")


class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_integration.csv"
        self.csv_handler = File(self.test_file)
        self.student_list = StudentList()
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_full_workflow(self):
        """Тест повного робочого циклу"""
        ############ Створення початкових студентів ##############
        initial_students = [Student("Anna", "+380501111111", "anna@gmail.com", "КБ-241")]
        
        ################ Запис у файл ##############
        self.csv_handler.write(initial_students)
        self.student_list.students = self.csv_handler.read()
        self.assertEqual(len(self.student_list.students), 1)
        
        ######### Додавання нового студента #############
        with patch("builtins.input", side_effect=["Victor", "+380503333333", "victor@gmail.com", "КБ-242"]):
            self.student_list.addNewElement()
        
        ############## Збереження оновленого списку у файл ##############
        self.csv_handler.write(self.student_list.students)
        
        ############ Повторне зчитування та перевірка #############
        final_students = self.csv_handler.read()
        self.assertEqual(len(final_students), 2)
        self.assertEqual(final_students[0].name, "Anna")
        self.assertEqual(final_students[1].name, "Victor")
    
    def test_add_update_delete_workflow(self):
        """Тест циклу додавання, оновлення та видалення"""
        ############ Початкові дані студента ##############
        initial_students = [
            Student("Bob", "+380501111111", "bob@gmail.com", "КБ-241"),
            Student("Charlie", "+380502222222", "charlie@gmail.com", "КБ-242")
        ]
        self.student_list.students = initial_students
        
        ############ Додавання студента ##############
        with patch("builtins.input", side_effect=["Alice", "+380503333333", "alice@gmail.com", "КБ-242"]):
            self.student_list.addNewElement()
        
        self.assertEqual(len(self.student_list.students), 3)
        
        ############ Оновлення студента ############
        with patch("builtins.input", side_effect=["Bob", "Bob_Updated", "+380509999999", "bob_new@gmail.com", "КБ-245"]):
            self.student_list.updateElement()
        
        names = [s.name for s in self.student_list.students]
        self.assertIn("Bob_Updated", names)
        self.assertNotIn("Bob", names)
        
        ################# Видалення студента #################
        with patch("builtins.input", return_value="Charlie"):
            self.student_list.deleteElement()
        
        self.assertEqual(len(self.student_list.students), 2)
        names = [s.name for s in self.student_list.students]
        self.assertNotIn("Charlie", names)
        
        ############ Перевірка залишку списку студентів ############
        self.assertIn("Alice", names)
        self.assertIn("Bob_Updated", names)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)