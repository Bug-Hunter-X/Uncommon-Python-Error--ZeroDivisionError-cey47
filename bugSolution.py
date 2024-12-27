def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Returns positive infinity if a is 0
        #Alternatively, you can raise a more descriptive exception:
        #raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a / b

result = function_with_uncommon_error(0, 10)
print(result) # Output: inf