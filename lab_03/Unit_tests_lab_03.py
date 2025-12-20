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
            Student("Andriy", "+380501111111", "andriy@gmail.com", "КБ-241"),
            Student("Maria", "+380502222222", "maria@gmail.com", "КБ-242")
        ]
    
    def test_addNewElement(self):

        initial_count = len(self.student_list.students)
        

        with patch("builtins.input", side_effect=["Oleg", "+380503333333", "oleg@gmail.com", "КБ-243"]):
            self.student_list.addNewElement()
        
        self.assertEqual(len(self.student_list.students), initial_count + 1)
        names = [s.name for s in self.student_list.students]
        self.assertIn("Oleg", names)
      
        self.assertTrue(names.index("Andriy") < names.index("Maria") < names.index("Oleg"))
    
    def test_deleteElement_found(self):
    
        initial_count = len(self.student_list.students)
        
        with patch("builtins.input", return_value="Andriy"):
            self.student_list.deleteElement()
        
        self.assertEqual(len(self.student_list.students), initial_count - 1)
        names = [s.name for s in self.student_list.students]
        self.assertNotIn("Andriy", names)
    
    def test_updateElement_found_and_resorted(self):

   
        with patch("builtins.input", side_effect=["Andriy", "Aaron", "+380509999999", "aaron@gmail.com", "КБ-245"]):
            self.student_list.updateElement()
        
        names = [s.name for s in self.student_list.students]
        self.assertIn("Aaron", names)
        self.assertNotIn("Andriy", names)
        

        self.assertEqual(names[0], "Aaron")
        self.assertEqual(names[1], "Maria") 

        updated_student = self.student_list.students[0]
        self.assertEqual(updated_student.phone, "+380509999999")



class TestFileHandler(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_students_top5.csv"
        self.csv_handler = File(self.test_file)
        
        self.students = [
            Student("Ivan", "+380501234567", "ivan@gmail.com", "КБ-241"),
            Student("Maria", "+380509876543", "maria@gmail.com", "КБ-242")
        ]
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_read_write_cycle(self):
    
        self.csv_handler.write(self.students)
        read_students = self.csv_handler.read()
        
        self.assertEqual(len(read_students), len(self.students))
        
      
        for i in range(len(self.students)):
            self.assertEqual(read_students[i].name, self.students[i].name)
            self.assertIsInstance(read_students[i], Student)



class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_integration_top5.csv"
        self.csv_handler = File(self.test_file)
        self.student_list = StudentList()
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_full_workflow(self):
       
        initial_students = [Student("Anna", "+380501111111", "anna@gmail.com", "КБ-241")]
        
    
        self.csv_handler.write(initial_students)
        self.student_list.students = self.csv_handler.read()
        self.assertEqual(len(self.student_list.students), 1)
        
     
        with patch("builtins.input", side_effect=["Victor", "+380503333333", "victor@gmail.com", "КБ-242"]):
            self.student_list.addNewElement()
        
 
        self.csv_handler.write(self.student_list.students)
        
 
        final_students = self.csv_handler.read()
        self.assertEqual(len(final_students), 2)
        self.assertEqual(final_students[0].name, "Anna")
        self.assertEqual(final_students[1].name, "Victor")


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)