import logging
from datetime import datetime

# Налаштування логування
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

def log_operation(operation_name, a, b, result):
    """Логування успішної операції"""
    logging.info(f"Операція: {operation_name}, Числа: {a} та {b}, Результат: {result}")

def log_error(operation_name, a, b, error_message):
    """Логування помилки"""
    logging.error(f"Операція: {operation_name}, Числа: {a} та {b}, Результат: {error_message}")

def log_warning(message):
    """Логування попередження"""
    logging.warning(message)