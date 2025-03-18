import sys

def is_python_version_correct():
    """Check if Python version is 3.x and return True/False"""
    return sys.version_info.major == 3

def is_number_even(n):
    """Return True if the number is even, else False"""
    return n % 2 == 0

def main():
    print("Running tests in hello_world.py...\n")

    # Test 2: Check if a number is even
    test_number = 4  # Change this number to test different cases
    if is_number_even(test_number):
        print(f" {test_number} is even")
    else:
        print(f" {test_number} is not even")
        sys.exit(1)  # Exit with error

    print("\n All tests passed successfully!")
    sys.exit(0)  # Exit successfully

if __name__ == "__main__":
    main()
