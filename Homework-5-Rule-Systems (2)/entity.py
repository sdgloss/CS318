class Entity:
    """An entity in a domain."""

    def __init__(self, name, entity_type):
        """Initialize an Entity type."""
        self.name = name
        self.type = entity_type

    def __str__(self):
        """Return string representation."""
        return f"{self.name}:{self.type}"

    def __repr__(self):
        """Return string representation."""
        return self.__str__()
