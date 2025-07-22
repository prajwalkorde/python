# Define the custom exception class
class AgeException(Exception):
    def __init__(self, message="Invalid age provided"):
        self.message = message
        super().__init__(self.message)

# Function to validate age
def validate_age(age):
    if age < 0 or age > 120:
        raise AgeException(f"Age {age} is not valid. Age must be between 0 and 120.")

# Example usage
try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)
    print(f"Your age is {user_age}.")
except AgeException as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")
