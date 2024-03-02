def reverse_integer(number):
    # Convert the number to a string and reverse it
    reversed_str = str(number)[::-1]

    # Convert the reversed string back to an integer
    
    return reversed_str

# Example usage
original_number = input()
reversed_number = reverse_integer(original_number)

print(f"Original number: {original_number}")
print(f"Reversed number: {reversed_number}")

