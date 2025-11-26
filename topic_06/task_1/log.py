def log_operation(operation_name, a, b, result):
    """Логування операції"""
    symbols = {
        'Додавання': '+',
        'Віднімання': '-',
        'Множення': '*',
        'Ділення': '/'
    }
    
    symbol = symbols.get(operation_name, '?')
    
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f"{a} {symbol} {b} = {result}\n")