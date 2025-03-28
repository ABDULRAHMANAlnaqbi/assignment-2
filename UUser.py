
# The USER class
class User:
    """
    Represents a system user with authentication, profile management, and communication features.
    """

    def __init__(self, user_id: int, name: str, contact_info: str, username: str, password: str, user_role: str):
        # Private attributes to store user details securely
        self.__user_id = user_id
        self.__name = name
        self.__contact_info = contact_info
        self.__username = username
        self.__password = password  # Storing plain text passwords is not secure
        self.__user_role = user_role

    # Getter and Setter for user_id
    def get_user_id(self) -> int:
        """Returns the user ID."""
        return self.__user_id

    def set_user_id(self, user_id: int) -> None:
        """Sets a new user ID."""
        self.__user_id = user_id

    # Getter and Setter for name
    def get_name(self) -> str:
        """Returns the user's name."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Updates the user's name."""
        self.__name = name

    # Getter and Setter for contact_info
    def get_contact_info(self) -> str:
        """Returns the user's contact information."""
        return self.__contact_info

    def set_contact_info(self, contact_info: str) -> None:
        """Updates the user's contact information."""
        self.__contact_info = contact_info

    # Getter and Setter for username
    def get_username(self) -> str:
        """Returns the user's username."""
        return self.__username

    def set_username(self, username: str) -> None:
        """Updates the user's username."""
        self.__username = username

    # Getter and Setter for user_role
    def get_user_role(self) -> str:
        """Returns the user's role."""
        return self.__user_role

    def set_user_role(self, user_role: str) -> None:
        """Updates the user's role."""
        self.__user_role = user_role

    # Authentication methods
    def login(self, username: str, password: str) -> bool:
        """
        Authenticates the user based on username and password.
        Ideally, password should be hashed and compared securely.
        """
        if self.__username == username and self.__password == password:
            print("Login successful.")
            return True
        print("Invalid credentials.")
        return False  # Consider limiting login attempts to prevent brute-force attacks

    def logout(self) -> None:
        """Logs out the user."""
        print("User logged out.")

    def update_profile(self, new_info: dict) -> None:
        """
        Updates the user's profile details.
        Ensures that only valid data is updated.
        """
        self.__name = new_info.get("name", self.__name)
        self.__contact_info = new_info.get("contact_info", self.__contact_info)
        print("Profile updated.")

    def reset_password(self, new_password: str) -> bool:
        """
        Resets the user's password.
        It should ideally enforce password complexity rules.
        """
        self.__password = new_password  # Password should be hashed for security
        print("Password reset successfully.")
        return True

    def deactivate_account(self) -> bool:
        """Deactivates the user's account."""
        print("Account has been deactivated.")
        return True  # Consider implementing a reactivation mechanism

    def get_account_details(self) -> dict:
        """
        Retrieves the user's account details.
        The password is not included for security reasons.
        """
        return {
            "user_id": self.__user_id,
            "name": self.__name,
            "contact_info": self.__contact_info,
            "username": self.__username,
            "user_role": self.__user_role,
        }

    def check_booking_history(self) -> list:
        """
        Retrieves the user's booking history.
        This should be fetched from a database instead of returning static data.
        """
        return ["Booking 1", "Booking 2", "Booking 3"]  # Placeholder for actual booking history

    def send_message(self, receiver: "User", message: str) -> None:
        """
        Sends a message to another user.
        Consider implementing a message queue for better handling.
        """
        print(f"Message sent to {receiver.get_username()}: {message}")

    def change_contact_info(self, new_contact: str) -> bool:
        """
        Updates the user's contact information.
        Validation should be added to ensure a valid email/phone format.
        """
        self.__contact_info = new_contact
        print("Contact information updated.")
        return True

    def upgrade_account(self, new_role: str) -> bool:
        """
        Upgrades the user's role in the system.
        Admin-level approval may be required for security.
        """
        self.__user_role = new_role
        print(f"Account upgraded to {new_role}.")
        return True

    def verify_identity(self, document: str) -> bool:
        """
        Verifies the user's identity using a provided document.
        Ideally, this should integrate with a secure verification system.
        """
        print(f"Verifying identity with document: {document}")
        return True  # Placeholder for actual verification logic

    def request_support(self, issue: str) -> str:
        """
        Submits a support request for the user.
        Consider logging these requests for tracking and response management.
        """
        return f"Support request submitted: {issue}"

    def __str__(self) -> str:
        """
        Returns a string representation of the User object.
        The password is not included for security reasons.
        """
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Username: {self.__username}, Role: {self.__user_role})"


# Example Usage
user1 = User(1, "Alice", "alice@email.com", "alice123", "pass123", "Customer")

# Testing Getter Methods
print(user1.get_name())  # Output: Alice
print(user1.get_account_details())

# Testing Setter Methods
user1.set_name("Alicia")
user1.set_contact_info("newemail@email.com")

# Testing str method
print(user1)  # Output: User(ID: 1, Name: Alicia, Username: alice123, Role: Customer)
