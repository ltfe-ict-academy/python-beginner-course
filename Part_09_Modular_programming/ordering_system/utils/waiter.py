class Waiter:
    """Waiter is serving tables."""

    def __init__(self, waiter_id: int, name: str) -> None:
        """Initialize the Waiter."""
        self.waiter_id = waiter_id
        self.name = name

    def __str__(self) -> str:
        """Create string representation of the object."""
        return f"Waiter {self.name} (id={self.waiter_id})"
