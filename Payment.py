
# Payment Class 
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
