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
