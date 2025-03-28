
# Employee class
class Employee:
    """
    Represents an employee responsible for handling service
    requests, managing schedules, and reporting work progress.
    """

    def __init__(self, employee_id: int, name: str, role: str, admin_id: int, username: str, password: str):
        # Private attributes for employee information
        self.__employee_id = employee_id
        self.__name = name
        self.__role = role
        self.__assigned_requests = []  # List to store assigned service requests
        self.__admin_id = admin_id  # ID of the admin supervising this employee
        self.__username = username
        self.__password = password  # Password should be stored securely (hashed)

    # Getter and Setter for employee_id
    def get_employee_id(self) -> int:
        """Returns the employee ID."""
        return self.__employee_id

    def set_employee_id(self, employee_id: int) -> None:
        """Sets a new employee ID."""
        self.__employee_id = employee_id

    # Getter and Setter for name
    def get_name(self) -> str:
        """Returns the employee's name."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Updates the employee's name."""
        self.__name = name

    # Getter and Setter for role
    def get_role(self) -> str:
        """Returns the employee's role."""
        return self.__role

    def set_role(self, role: str) -> None:
        """Updates the employee's role."""
        self.__role = role

    # Getter and Setter for assigned requests
    def get_assigned_requests(self) -> list:
        """Returns a list of assigned service requests."""
        return self.__assigned_requests

    def assign_request(self, request_id: int) -> None:
        """Assigns a service request to the employee."""
        self.__assigned_requests.append(request_id)
        print(f"Request {request_id} assigned to {self.__name}.")

    # Getter and Setter for admin_id
    def get_admin_id(self) -> int:
        """Returns the ID of the supervising admin."""
        return self.__admin_id

    def set_admin_id(self, admin_id: int) -> None:
        """Sets a new admin ID."""
        self.__admin_id = admin_id

    # Getter and Setter for username
    def get_username(self) -> str:
        """Returns the employee's username."""
        return self.__username

    def set_username(self, username: str) -> None:
        """Updates the employee's username."""
        self.__username = username

    # Employee actions
    def handle_service_request(self, request_id: int) -> None:
        """Processes a service request."""
        print(f"Handling service request {request_id}.")

    def update_request_status(self, request_id: int, status: str) -> None:
        """Updates the status of a service request."""
        print(f"Service request {request_id} status updated to {status}.")

    def view_schedule(self) -> dict:
        """Retrieves the employee's schedule."""
        return {"Monday": "Shift 9 AM - 5 PM", "Tuesday": "Off-duty"}

    def submit_work_report(self) -> None:
        """Submits a work report."""
        print("Work report submitted.")

    def request_leave(self, days: int) -> bool:
        """Allows an employee to request leave."""
        if days <= 14:
            print("Leave request approved.")
            return True
        print("Leave request denied.")
        return False

    def receive_notification(self, message: str) -> None:
        """Receives a notification."""
        print(f"Notification received: {message}")

    def log_hours_worked(self, hours: int) -> None:
        """Logs the number of hours worked by the employee."""
        print(f"Logged {hours} hours worked.")

    def transfer_request_to_another_employee(self, employee: "Employee", request_id: int) -> None:
        """Transfers a service request to another employee."""
        print(f"Transferred request {request_id} to {employee.get_name()}")

    def view_employee_performance(self) -> dict:
        """Retrieves performance metrics of the employee."""
        return {"Performance": "Excellent", "Tasks Completed": 50}

    def __str__(self) -> str:
        """Returns a string representation of the Employee object."""
        return f"Employee(ID: {self.__employee_id}, Name: {self.__name}, Role: {self.__role}, Username: {self.__username})"


# Example Usage
employee1 = Employee(101, "John Doe", "Technician", 5001, "johndoe", "securepass")

# Testing Getter Methods
print(employee1.get_name())  # Output: John Doe
print(employee1.get_employee_id())  # Output: 101
print(employee1.get_role())  # Output: Technician
print(employee1.get_assigned_requests())  # Output: []

# Testing Setter Methods
employee1.set_name("Johnny Doe")
employee1.set_role("Senior Technician")

# Assign a request
employee1.assign_request(2001)

# Testing str method
print(employee1)  # Output: Employee(ID: 101, Name: Johnny Doe, Role: Senior Technician, Username: johndoe)
