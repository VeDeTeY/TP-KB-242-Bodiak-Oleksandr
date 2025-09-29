def list_testing():
    
    numbers = [5, 2, 9]
    print("Початковий список:", numbers)
    
    # append()
    numbers.append(7)
    print("Після append(7):", numbers)
    
    # extend()
    numbers.extend([1, 3])
    print("Після extend([1, 3]):", numbers)
    
    # insert()
    numbers.insert(2, 100)
    print("Після insert(2, 100):", numbers)
    
    # remove()
    numbers.remove(100)
    print("Після remove(100):", numbers)
    
    # copy()
    numbers_copy = numbers.copy()
    print("Копія списку:", numbers_copy)
    
    # sort()
    numbers.sort()
    print("Після sort():", numbers)
    
    # reverse()
    numbers.reverse()
    print("Після reverse():", numbers)
    
    # clear()
    numbers.clear()
    print("Після clear():", numbers)


list_testing()
