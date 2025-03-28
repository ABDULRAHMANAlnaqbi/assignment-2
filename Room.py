
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
