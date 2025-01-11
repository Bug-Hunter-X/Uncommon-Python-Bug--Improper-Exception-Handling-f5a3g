def function_with_uncommon_bug(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None #This is important to handle the exception properly
    except TypeError:
        print("Unsupported operand type(s) for /: 'int' and 'str'")
        return None
    else:
        return result

# Example usage
print(function_with_uncommon_bug(10, 2)) # Output: 5.0
print(function_with_uncommon_bug(10, 0)) # Output: Cannot divide by zero! None
print(function_with_uncommon_bug(10, "hello")) # Output: Unsupported operand type(s) for /: 'int' and 'str' None