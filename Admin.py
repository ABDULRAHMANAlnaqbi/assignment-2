
# Admin class 
class Admin:
    """
    Represents an administrative user who manages hotel operations.
    """

    def __init__(self, admin_id: int, username: str, password: str):
        """
        Initializes an Admin instance.

        :param admin_id: Unique identifier for the admin.
        :param username: Admin's username.
        :param password: Admin's password (should be securely stored in a real application).
        """
        self.__admin_id = admin_id
        self.__username = username
        self.__password = password  # Consider using a hashing function for security.

    # Getter and Setter for admin_id
    def get_admin_id(self) -> int:
        """Returns the admin ID."""
        return self.__admin_id

    def set_admin_id(self, admin_id: int) -> None:
        """Updates the admin ID."""
        self.__admin_id = admin_id

    # Getter and Setter for username
    def get_username(self) -> str:
        """Returns the admin's username."""
        return self.__username

    def set_username(self, username: str) -> None:
        """Updates the admin's username."""
        self.__username = username

    # Getter and Setter for password
    def get_password(self) -> str:
        """Returns the admin's password (not recommended for security reasons)."""
        return self.__password

    def set_password(self, password: str) -> None:
        """Updates the admin's password (should be hashed for security)."""
        self.__password = password

    def manage_rooms(self) -> None:
        """Manages hotel rooms, such as adding or removing rooms."""
        print("Managing rooms...")

    def view_reports(self) -> str:
        """Retrieves and displays system reports."""
        return "Displaying system reports..."

    def approve_service_requests(self, request_id: int) -> None:
        """Approves a service request based on its ID."""
        print(f"Service request {request_id} approved.")

    def assign_employees_to_requests(self) -> None:
        """Assigns employees to handle specific service requests."""
        print("Assigning employees to service requests...")

    def monitor_system_activity(self) -> dict:
        """Monitors the system's current activity, including status and active users."""
        return {"status": "System running smoothly", "active_users": 120}

    def update_hotel_policies(self, policy: str) -> None:
        """Updates hotel policies."""
        print(f"Updated hotel policy: {policy}")

    def generate_financial_report(self) -> str:
        """Generates a financial report for the hotel."""
        return "Financial report generated."

    def block_guest(self, guest_id: int) -> None:
        """Blocks a guest from making further bookings."""
        print(f"Guest {guest_id} has been blocked.")

    def change_room_prices(self, new_price: float, room_type: str) -> None:
        """Updates the price for a specific type of room."""
        print(f"Updated price of {room_type} rooms to {new_price}.")

    def add_new_employee(self, employee: "Employee") -> None:
        """Adds a new employee to the system."""
        print(f"New employee {employee.get_name()} added to the system.")

    def remove_employee(self, employee_id: int) -> None:
        """Removes an employee from the system."""
        print(f"Employee with ID {employee_id} has been removed.")

    def __str__(self) -> str:
        """Returns a string representation of the Admin object."""
        return f"Admin(ID: {self.__admin_id}, Username: {self.__username})"


# Example Usage
admin1 = Admin(1, "admin123", "securepass")

# Testing Getter Methods
print(admin1.get_admin_id())  # Output: 1
print(admin1.get_username())  # Output: admin123

# Testing Setter Methods
admin1.set_username("superadmin")
admin1.set_password("newsecurepass")

# Printing Updated Admin Info
print(admin1)  # Output: Admin(ID: 1, Username: superadmin)
