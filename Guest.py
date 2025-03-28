# Guest class
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
