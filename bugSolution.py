def function_with_uncommon_bug(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return 0 # return 0 or a default value to handle the division by zero case
    except TypeError:
        print("Unsupported operand type(s) for /: 'int' and 'str'")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0 # Handle other potential exceptions
    else:
        return result

# Example usage
print(function_with_uncommon_bug(10, 2)) # Output: 5.0
print(function_with_uncommon_bug(10, 0)) # Output: Cannot divide by zero! 0
print(function_with_uncommon_bug(10, "hello")) # Output: Unsupported operand type(s) for /: 'int' and 'str' 0