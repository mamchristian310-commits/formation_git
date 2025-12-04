def pyramid(n):
    """Generate a pyramid pattern of asterisks with n levels."""
    for i in range(1, n + 1):
        # Print leading spaces
        print(' ' * (n - i), end='')
        # Print asterisks
        print('* ' * i)
        
# Example usage
pyramid(10)