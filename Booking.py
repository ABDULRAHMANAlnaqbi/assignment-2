
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
        print(f"Booking {self.__booking_id} assigned to Room {room.get_room_number()}")

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
