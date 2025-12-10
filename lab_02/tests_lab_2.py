import unittest
import lab_2
from unittest.mock import patch
from io import StringIO


class TestStudentSystem(unittest.TestCase):
    def setUp(self):
        """Підготовка тестових даних перед кожним тестом"""
        self.student_list = []

    # ==================== Виведення всього списку ====================
    def test_printAllList(self):
        """Вивід списку студентів"""
        self.student_list = [
            {"name": "Alice", "phone": "1233458753", "email": "alice@gmail.com", "group": "КБ-242"}    ]
        with patch("sys.stdout", new_callable=StringIO) as fake_output:
            lab_2.printAllList(self.student_list)
            output = fake_output.getvalue().strip()
        
        expected = "Name: Alice, Phone: 1233458753, Email: alice@gmail.com, Group: КБ-242\n===================================="
        self.assertEqual(output, expected)

    # ==================== додавання нового елементу ====================
    def test_addNewElement(self):
        """Додавання нового студента"""
        self.student_list = [
            {"name": "Bob", "phone": "4563398892", "email": "bob@gmail.com", "group": "КБ-241"}
        ]
        with patch("builtins.input", side_effect=["Alice", "1233458753", "alice@gmail.com", "КБ-242"]):
            lab_2.addNewElement(self.student_list)
        
        self.assertEqual(len(self.student_list), 2)
        self.assertEqual(self.student_list[0]["name"], "Alice")

    # ==================== Видалення існуючого елемента ====================
    def test_deleteElement(self):
        """Видалення існуючого студента"""
        self.student_list = [
            {"name": "Bob", "phone": "4563398892", "email": "bob@gmail.com", "group": "КБ-241"}
        ]
        with patch("builtins.input", return_value="Bob"):
            lab_2.deleteElement(self.student_list)
        
        self.assertEqual(len(self.student_list), 0)

    def test_deleteElement_not_found(self):
        """Тест видалення неіснуючого студента"""
        self.student_list = [
            {"name": "Bob", "phone": "4563398892", "email": "bob@gmail.com", "group": "КБ-241"}
        ]
        with patch("builtins.input", return_value="Alice"):
            lab_2.deleteElement(self.student_list)
        
        self.assertEqual(len(self.student_list), 1)

    # ==================== Оновлення нового елемента ====================
    def test_updateElement_found(self):
        """Оновлення існуючого студента"""
        self.student_list = [
            {"name": "Bob", "phone": "4563398892", "email": "bob@gmail.com", "group": "КБ-241"}
        ]
        with patch("builtins.input", side_effect=["Bob", "Bob_Updated", "999", "bob_new@gmail.com", "КБ-242"]):
            lab_2.updateElement(self.student_list)
        
        self.assertEqual(len(self.student_list), 1)
        self.assertEqual(self.student_list[0]["name"], "Bob_Updated")

    def test_updateElement_not_found(self):
        """Оновлення неіснуючого студента"""
        self.student_list = [
            {"name": "Bob", "phone": "4563398892", "email": "bob@gmail.com", "group": "КБ-241"}
        ]
        with patch("builtins.input", return_value="Alice"):
            lab_2.updateElement(self.student_list)
        
        self.assertEqual(len(self.student_list), 1)


if __name__ == "__main__":
    unittest.main()