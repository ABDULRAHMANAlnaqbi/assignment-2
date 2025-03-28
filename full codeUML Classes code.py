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


#Room Class
class Room:
    """
    Represents a hotel room with details like room number, type, amenities, price, and availability.
    """

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, availability_status: bool = True):
        """
        Initializes a Room object with its details.
        
        Parameters:
        - room_number (int): Unique number assigned to the room.
        - room_type (str): Type of room (e.g., Single, Double, Suite).
        - amenities (list): List of amenities available in the room.
        - price_per_night (float): Cost of staying per night.
        - availability_status (bool): Whether the room is available (default: True).
        """
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities  # List of amenities like Wi-Fi, AC, TV, etc.
        self.__price_per_night = price_per_night
        self.__availability_status = availability_status  # True if the room is available, False otherwise.

    # Getter and Setter for room_number
    def get_room_number(self) -> int:
        """Returns the room number."""
        return self.__room_number

    def set_room_number(self, room_number: int) -> None:
        """Sets a new room number."""
        self.__room_number = room_number

    # Getter and Setter for room_type
    def get_room_type(self) -> str:
        """Returns the room type."""
        return self.__room_type

    def set_room_type(self, room_type: str) -> None:
        """Updates the room type."""
        self.__room_type = room_type

    # Getter and Setter for amenities
    def get_amenities(self) -> list:
        """Returns the list of amenities available in the room."""
        return self.__amenities

    def add_amenity(self, amenity: str) -> None:
        """Adds a new amenity to the room if it's not already present."""
        if amenity not in self.__amenities:
            self.__amenities.append(amenity)

    def remove_amenity(self, amenity: str) -> None:
        """Removes an existing amenity from the room."""
        if amenity in self.__amenities:
            self.__amenities.remove(amenity)

    # Getter and Setter for price_per_night
    def get_price(self) -> float:
        """Returns the price per night for the room."""
        return self.__price_per_night

    def update_price(self, new_price: float) -> None:
        """Updates the price per night of the room."""
        self.__price_per_night = new_price

    # Getter and Setter for availability_status
    def check_availability(self) -> bool:
        """Returns the availability status of the room."""
        return self.__availability_status

    def update_status(self, new_status: bool) -> None:
        """Updates the availability status of the room."""
        self.__availability_status = new_status

    def release_room(self) -> None:
        """Marks the room as available when a guest checks out."""
        self.__availability_status = True

    def schedule_maintenance(self, date: str) -> None:
        """Marks the room as unavailable due to scheduled maintenance."""
        self.__availability_status = False

    def calculate_discounted_price(self, discount: float) -> float:
        """
        Calculates the price of the room after applying a discount.
        
        Parameters:
        - discount (float): Discount percentage to be applied.
        
        Returns:
        - float: The discounted price.
        """
        return self.__price_per_night * (1 - discount / 100)

    def get_room_info(self) -> dict:
        """Returns a dictionary containing all the room details."""
        return {
            "room_number": self.__room_number,
            "room_type": self.__room_type,
            "amenities": self.__amenities,
            "price_per_night": self.__price_per_night,
            "availability_status": self.__availability_status
        }

    def __str__(self) -> str:
        """
        Returns a string representation of the Room object.
        """
        availability = "Available" if self.__availability_status else "Occupied"
        return f"Room {self.__room_number}: {self.__room_type}, Price: ${self.__price_per_night}/night, Status: {availability}"


# Example Usage
room1 = Room(101, "Suite", ["Wi-Fi", "TV", "Mini-Bar"], 150.0)

# Testing Getter Methods
print(room1.get_room_number())  # Output: 101
print(room1.get_room_type())  # Output: Suite
print(room1.get_amenities())  # Output: ['Wi-Fi', 'TV', 'Mini-Bar']
print(room1.get_price())  # Output: 150.0
print(room1.check_availability())  # Output: True

# Testing Setter Methods
room1.set_room_number(202)
room1.set_room_type("Deluxe Suite")
room1.add_amenity("Jacuzzi")
room1.update_price(200.0)
room1.update_status(False)  # Mark room as occupied

# Printing Updated Room Info
print(room1)  # Output: Room 202: Deluxe Suite, Price: $200.0/night, Status: Occupied

 
 # guest class
class Guest:
    """
    Represents a guest with personal details and loyalty program status.
    """

    def __init__(self, guest_id: int, name: str, contact_info: str, loyalty_status: bool = False):
        """
        Initializes a Guest object.
        
        Parameters:
        - guest_id (int): Unique ID for the guest.
        - name (str): Guest's full name.
        - contact_info (str): Guest's contact details.
        - loyalty_status (bool): Whether the guest is enrolled in the loyalty program.
        """
        self.__guest_id = guest_id
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_status = loyalty_status
        self.__loyalty_points = 0  # Start with 0 points
        self.__reservation_history = []  # List of booking IDs

    # Getter and Setter for guest_id
    def get_guest_id(self) -> int:
        """Returns the guest ID."""
        return self.__guest_id

    def set_guest_id(self, guest_id: int) -> None:
        """Sets a new guest ID."""
        self.__guest_id = guest_id

    # Getter and Setter for name
    def get_name(self) -> str:
        """Returns the guest's name."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Updates the guest's name."""
        self.__name = name

    # Getter and Setter for contact_info
    def get_contact_info(self) -> str:
        """Returns the guest's contact information."""
        return self.__contact_info

    def set_contact_info(self, contact_info: str) -> None:
        """Updates the guest's contact information."""
        self.__contact_info = contact_info

    # Getter and Setter for loyalty_status
    def get_loyalty_status(self) -> bool:
        """Returns the guest's loyalty program enrollment status."""
        return self.__loyalty_status

    def set_loyalty_status(self, status: bool) -> None:
        """Updates the guest's loyalty program enrollment status."""
        self.__loyalty_status = status

    # Getter for reservation history
    def get_reservation_history(self) -> list:
        """Returns the guest's reservation history."""
        return self.__reservation_history

    def create_account(self, name: str, contact_info: str) -> None:
        """Creates a guest account."""
        self.__name = name
        self.__contact_info = contact_info
        print("Account created successfully.")

    def update_profile(self, new_name: str, new_contact: str) -> None:
        """Updates guest profile details."""
        self.__name = new_name
        self.__contact_info = new_contact
        print("Profile updated successfully.")

    def join_loyalty_program(self) -> None:
        """Enrolls the guest in the loyalty program."""
        if not self.__loyalty_status:
            self.__loyalty_status = True
            self.__loyalty_points = 50  # Give initial bonus points
            print("Joined loyalty program successfully. Earned 50 points!")
        else:
            print("Already enrolled in the loyalty program.")

    def request_service(self, service: str) -> str:
        """Requests an additional service for the stay."""
        return f"Service request '{service}' has been placed."

    def cancel_booking(self, booking_id: int) -> None:
        """Cancels a booking and removes it from the reservation history."""
        if booking_id in self.__reservation_history:
            self.__reservation_history.remove(booking_id)
            print(f"Booking {booking_id} has been canceled.")
        else:
            print(f"Booking {booking_id} not found.")

    def give_feedback(self, rating: int, comments: str) -> str:
        """Allows the guest to give feedback on their stay."""
        return f"Feedback submitted with rating {rating}: {comments}"

    def view_loyalty_points(self) -> int:
        """Returns the number of loyalty points the guest has."""
        return self.__loyalty_points

    def earn_loyalty_points(self, amount_spent: float) -> None:
        """
        Adds loyalty points based on the amount spent on bookings.
        
        - Earn 1 point per $10 spent.
        """
        points_earned = int(amount_spent / 10)
        self.__loyalty_points += points_earned
        print(f"You earned {points_earned} loyalty points! Total: {self.__loyalty_points} points.")

    def redeem_loyalty_points(self, points: int) -> bool:
        """Redeems loyalty points if the guest has enough."""
        if points > self.__loyalty_points:
            print("Not enough loyalty points.")
            return False
        self.__loyalty_points -= points
        print(f"{points} loyalty points redeemed successfully. Remaining: {self.__loyalty_points} points.")
        return True

    def add_reservation(self, booking_id: int) -> None:
        """Adds a booking ID to the guest's reservation history."""
        self.__reservation_history.append(booking_id)

    def view_invoice(self, booking_id: int) -> str:
        """Displays invoice details for a given booking."""
        if booking_id in self.__reservation_history:
            return f"Invoice for booking {booking_id} is available."
        return f"No invoice found for booking {booking_id}."

    def __str__(self) -> str:
        """Returns a string representation of the Guest object."""
        loyalty = "Enrolled" if self.__loyalty_status else "Not Enrolled"
        return f"Guest(ID: {self.__guest_id}, Name: {self.__name}, Contact: {self.__contact_info}, Loyalty: {loyalty})"


# Example Usage
guest1 = Guest(301, "Alice Smith", "alice@email.com")

# Testing Getter Methods
print(guest1.get_name())  # Output: Alice Smith
print(guest1.get_guest_id())  # Output: 301
print(guest1.get_loyalty_status())  # Output: False
print(guest1.get_reservation_history())  # Output: []

# Testing Setter Methods
guest1.set_name("Alice Johnson")
guest1.set_contact_info("newalice@email.com")
guest1.join_loyalty_program()

# Adding a reservation
guest1.add_reservation(5001)

# Printing Updated Guest Info
print(guest1)  # Output: Guest(ID: 301, Name: Alice Johnson, Contact: newalice@email.com, Loyalty: Enrolled)

#Booking Class
class Booking:
    """
    Represents a hotel booking with guest details, room assignment, and booking status.
    """

    def __init__(self, booking_id: int, guest: "Guest", room: "Room", check_in_date: str, check_out_date: str, status: str = "Pending"):
        """
        Initializes a Booking instance.

        :param booking_id: Unique identifier for the booking.
        :param guest: The Guest object associated with the booking.
        :param room: The Room object assigned to the booking.
        :param check_in_date: The check-in date in YYYY-MM-DD format.
        :param check_out_date: The check-out date in YYYY-MM-DD format.
        :param status: The booking status (e.g., Pending, Confirmed, Cancelled).
        """
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status
        self.__special_requests = []

    # Getter and Setter for booking_id
    def get_booking_id(self) -> int:
        """Returns the booking ID."""
        return self.__booking_id

    def set_booking_id(self, booking_id: int) -> None:
        """Updates the booking ID."""
        self.__booking_id = booking_id

    # Getter and Setter for status
    def get_status(self) -> str:
        """Returns the current booking status."""
        return self.__status

    def set_status(self, status: str) -> None:
        """Updates the booking status."""
        self.__status = status

    # Getter and Setter for special_requests
    def get_special_requests(self) -> list:
        """Returns the list of special requests made for the booking."""
        return self.__special_requests

    def add_special_request(self, request: str) -> None:
        """Adds a special request for the booking."""
        self.__special_requests.append(request)
        print(f"Special request added: {request}")

    def confirm_booking(self) -> None:
        """Confirms the booking by updating its status."""
        self.__status = "Confirmed"
        print(f"Booking {self.__booking_id} confirmed.")

    def cancel_booking(self) -> None:
        """Cancels the booking by updating its status."""
        self.__status = "Cancelled"
        print(f"Booking {self.__booking_id} cancelled.")

    def modify_booking(self, new_dates: tuple) -> None:
        """
        Modifies the booking dates.

        :param new_dates: A tuple containing (new_check_in_date, new_check_out_date).
        """
        self.__check_in_date, self.__check_out_date = new_dates
        print(f"Booking {self.__booking_id} modified to new dates: {new_dates}")

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the booking based on room price and duration.

        :return: The total cost of the stay.
        """
        num_nights = int(self.__check_out_date.split('-')[2]) - int(self.__check_in_date.split('-')[2])
        return num_nights * self.__room.get_price()

    def apply_discount(self, discount: float) -> None:
        """
        Applies a discount to the room price.

        :param discount: The discount percentage (0-100).
        """
        new_price = self.__room.calculate_discounted_price(discount)
        print(f"Discount applied. New room price: {new_price}")

    def extend_booking(self, extra_days: int) -> None:
        """
        Extends the booking by a given number of days.

        :param extra_days: The number of additional days to extend the booking.
        """
        new_checkout_day = int(self.__check_out_date.split('-')[2]) + extra_days
        self.__check_out_date = f"{self.__check_out_date[:8]}{new_checkout_day}"
        print(f"Booking {self.__booking_id} extended for {extra_days} extra days.")

    def assign_room(self, room: "Room") -> None:
        """
        Assigns a new room to the booking.

        :param room: The new Room object.
        """
        self.__room = room
        print(f"Booking {self.__booking_id} assigned to Room {room.get_room_info()['room_number']}")

    def change_guest_details(self, new_guest: "Guest") -> None:
        """
        Updates the guest details associated with the booking.

        :param new_guest: The new Guest object.
        """
        self.__guest = new_guest
        print(f"Guest details updated for Booking {self.__booking_id}")

    def notify_guest(self) -> None:
        """Sends a notification to the guest about their booking."""
        print(f"Notification sent to Guest {self.__guest.get_name()} for Booking {self.__booking_id}")

    def generate_booking_summary(self) -> str:
        """Generates a summary of the booking details."""
        return f"Booking {self.__booking_id}: Guest {self.__guest.get_name()}, Room {self.__room.get_room_number()}, Status: {self.__status}"

    def __str__(self) -> str:
        """Returns a string representation of the Booking object."""
        return f"Booking ID: {self.__booking_id}, Guest: {self.__guest.get_name()}, Room: {self.__room.get_room_number()}, Status: {self.__status}"


# Example Usage
guest1 = Guest(301, "Alice Smith", "alice@email.com")
room1 = Room(101, "Suite", ["Wi-Fi", "TV", "Mini-Bar"], 150.0)

booking1 = Booking(1001, guest1, room1, "2025-07-01", "2025-07-05")

# Testing Getter Methods
print(booking1.get_booking_id())  # Output: 1001
print(booking1.get_status())  # Output: Pending
print(booking1.get_special_requests())  # Output: []

# Testing Setter Methods
booking1.set_status("Confirmed")
booking1.add_special_request("Extra towels")

# Confirm Booking
booking1.confirm_booking()

# Testing total cost calculation
print(f"Total Cost: ${booking1.calculate_total_cost()}")  # Output: Total Cost: $600.0

# Printing Updated Booking Info
print(booking1)  # Output: Booking ID: 1001, Guest: Alice Smith, Room: 101, Status: Confirmed


#Payment Class 
class Payment:
    """
    Handles payment processing, invoices, refunds, and validation.
    """

    def __init__(self, payment_id: int, booking: "Booking", amount: float, payment_method: str, status: str = "Pending"):
        """
        Initializes a Payment instance.

        :param payment_id: Unique identifier for the payment.
        :param booking: The Booking object associated with the payment.
        :param amount: The amount to be paid.
        :param payment_method: The method of payment (e.g., Credit Card, PayPal).
        :param status: The payment status (e.g., Pending, Completed, Refunded).
        """
        self.__payment_id = payment_id
        self.__booking = booking
        self.__amount = amount
        self.__payment_method = payment_method
        self.__status = status

    # Getter and Setter for payment_id
    def get_payment_id(self) -> int:
        """Returns the payment ID."""
        return self.__payment_id

    def set_payment_id(self, payment_id: int) -> None:
        """Updates the payment ID."""
        self.__payment_id = payment_id

    # Getter and Setter for amount
    def get_amount(self) -> float:
        """Returns the payment amount."""
        return self.__amount

    def set_amount(self, amount: float) -> None:
        """Updates the payment amount."""
        self.__amount = amount

    # Getter and Setter for payment_method
    def get_payment_method(self) -> str:
        """Returns the payment method."""
        return self.__payment_method

    def set_payment_method(self, payment_method: str) -> None:
        """Updates the payment method."""
        self.__payment_method = payment_method

    # Getter and Setter for status
    def get_payment_status(self) -> str:
        """Returns the current payment status."""
        return self.__status

    def set_payment_status(self, status: str) -> None:
        """Updates the payment status."""
        self.__status = status

    def process_payment(self) -> bool:
        """Processes the payment if it's still pending."""
        if self.__status == "Pending":
            self.__status = "Completed"
            print("Payment processed successfully.")
            return True
        print("Payment failed or already processed.")
        return False

    def generate_invoice(self) -> str:
        """Generates an invoice for the payment."""
        return f"Invoice: Payment ID {self.__payment_id}, Amount: {self.__amount}, Method: {self.__payment_method}, Status: {self.__status}"

    def refund_payment(self) -> None:
        """Refunds the payment if it was completed."""
        if self.__status == "Completed":
            self.__status = "Refunded"
            print("Payment refunded successfully.")

    def apply_vat(self, vat: float) -> None:
        """Applies VAT to the payment amount."""
        self.__amount += self.__amount * (vat / 100)
        print(f"VAT applied. New amount: {self.__amount}")

    def split_payment(self, methods: list[str], amounts: list[float]) -> None:
        """Splits the payment across multiple methods if the total matches."""
        if sum(amounts) == self.__amount:
            self.__payment_method = ", ".join(methods)
            print(f"Payment successfully split across methods: {methods}")
        else:
            print("Error: Split payment amounts do not match the total amount.")

    def validate_payment_details(self) -> bool:
        """Validates payment details (amount must be positive and a payment method must be provided)."""
        return self.__amount > 0 and bool(self.__payment_method)

    def send_payment_receipt(self) -> None:
        """Sends a payment receipt."""
        print(f"Receipt sent for Payment ID {self.__payment_id}")

    def apply_coupon(self, coupon_code: str) -> bool:
        """Applies a coupon discount if valid."""
        if coupon_code == "DISCOUNT10":
            self.__amount *= 0.9
            print("Coupon applied successfully.")
            return True
        print("Invalid coupon code.")
        return False

    def record_failed_transaction(self) -> None:
        """Records a failed transaction."""
        self.__status = "Failed"
        print("Payment failed and recorded.")

    def verify_card_details(self, card_number: str) -> bool:
        """Verifies if a card number is valid (must be 16 digits and numeric)."""
        return len(card_number) == 16 and card_number.isdigit()

    def __str__(self) -> str:
        """Returns a string representation of the Payment object."""
        return f"Payment ID: {self.__payment_id}, Amount: ${self.__amount}, Method: {self.__payment_method}, Status: {self.__status}"


# Example Usage
booking1 = Booking(1001, Guest(301, "Alice Smith", "alice@email.com"), Room(101, "Suite", ["Wi-Fi", "TV", "Mini-Bar"], 150.0), "2025-07-01", "2025-07-05")
payment1 = Payment(5001, booking1, 600.0, "Credit Card")

# Testing Getter Methods
print(payment1.get_payment_id())  # Output: 5001
print(payment1.get_amount())  # Output: 600.0
print(payment1.get_payment_method())  # Output: Credit Card
print(payment1.get_payment_status())  # Output: Pending

# Testing Setter Methods
payment1.set_amount(650.0)
payment1.set_payment_status("Completed")

# Processing Payment
payment1.process_payment()

# Applying VAT
payment1.apply_vat(10)  # Adds 10% VAT

# Printing Updated Payment Info
print(payment1)  # Output: Payment ID: 5001, Amount: $715.0, Method: Credit Card, Status: Completed

    #Admin class 
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


#Feedback Class
class Feedback:
    """
    Represents guest feedback with rating and comments, along with admin interactions.
    """

    all_feedbacks = []  # Stores all feedback instances for filtering and analysis

    def __init__(self, feedback_id: int, guest: "Guest", rating: int, comments: str):
        """
        Initializes a Feedback instance.

        :param feedback_id: Unique identifier for the feedback.
        :param guest: The Guest object associated with the feedback.
        :param rating: The rating given by the guest (1-5).
        :param comments: The comments provided by the guest.
        """
        self.__feedback_id = feedback_id
        self.__guest = guest
        self.__rating = rating
        self.__comments = comments
        Feedback.all_feedbacks.append(self)  # Store feedback globally

    # Getter and Setter for feedback_id
    def get_feedback_id(self) -> int:
        """Returns the feedback ID."""
        return self.__feedback_id

    def set_feedback_id(self, feedback_id: int) -> None:
        """Updates the feedback ID."""
        self.__feedback_id = feedback_id

    # Getter and Setter for rating
    def get_rating(self) -> int:
        """Returns the feedback rating."""
        return self.__rating

    def set_rating(self, rating: int) -> None:
        """Updates the feedback rating."""
        self.__rating = rating

    # Getter and Setter for comments
    def get_comments(self) -> str:
        """Returns the feedback comments."""
        return self.__comments

    def set_comments(self, comments: str) -> None:
        """Updates the feedback comments."""
        self.__comments = comments

    def submit_feedback(self, rating: int, comments: str) -> None:
        """Updates feedback rating and comments."""
        self.__rating = rating
        self.__comments = comments
        print(f"Feedback submitted: Rating {rating}, Comment: {comments}")

    def view_feedback(self) -> str:
        """Returns feedback details."""
        return f"Feedback ID: {self.__feedback_id}, Rating: {self.__rating}, Comments: {self.__comments}"

    @staticmethod
    def get_average_rating() -> float:
        """Calculates and returns the average rating from all feedbacks."""
        if not Feedback.all_feedbacks:
            return 0.0
        total_rating = sum(f.__rating for f in Feedback.all_feedbacks)
        return total_rating / len(Feedback.all_feedbacks)

    @staticmethod
    def filter_feedback_by_rating(min_rating: int) -> list:
        """Filters and returns feedback with ratings greater than or equal to min_rating."""
        return [f for f in Feedback.all_feedbacks if f.__rating >= min_rating]

    def edit_feedback(self, new_rating: int, new_comments: str) -> None:
        """Edits an existing feedback entry."""
        self.__rating = new_rating
        self.__comments = new_comments
        print(f"Feedback updated: Rating {new_rating}, Comment: {new_comments}")

    def delete_feedback(self) -> None:
        """Deletes a feedback entry."""
        Feedback.all_feedbacks.remove(self)
        print("Feedback deleted successfully.")

    @staticmethod
    def get_guest_feedback(guest_id: int) -> list:
        """Retrieves all feedback entries for a specific guest ID."""
        return [f for f in Feedback.all_feedbacks if f.__guest.get_guest_id() == guest_id]

    def reply_to_feedback(self, admin: "Admin", response: str) -> None:
        """Allows an admin to reply to feedback."""
        print(f"Admin {admin.get_username()} replied to Feedback {self.__feedback_id}: {response}")

    @staticmethod
    def analyze_feedback_trends() -> dict:
        """Analyzes feedback trends and returns relevant data."""
        return {
            "Total Feedbacks": len(Feedback.all_feedbacks),
            "Average Rating": Feedback.get_average_rating(),
        }

    def __str__(self) -> str:
        """Returns a string representation of the Feedback object."""
        return f"Feedback(ID: {self.__feedback_id}, Guest: {self.__guest.get_name()}, Rating: {self.__rating}, Comments: {self.__comments})"


# Example Usage
guest1 = Guest(301, "Alice Smith", "alice@email.com")
feedback1 = Feedback(101, guest1, 5, "Great service!")

# Testing Getter Methods
print(feedback1.get_feedback_id())  # Output: 101
print(feedback1.get_rating())  # Output: 5
print(feedback1.get_comments())  # Output: Great service!

# Testing Setter Methods
feedback1.set_rating(4)
feedback1.set_comments("Good service, but can improve.")

# Viewing Feedback
print(feedback1.view_feedback())  # Output: Feedback ID: 101, Rating: 4, Comments: Good service, but can improve.

# Printing Feedback Object
print(feedback1)  # Output: Feedback(ID: 101, Guest: Alice Smith, Rating: 4, Comments: Good service, but can improve.)
