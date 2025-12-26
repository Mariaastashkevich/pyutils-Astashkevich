class JsonLoadError(Exception):
    """
    Raised when JSON file cannot be loaded
    """
    def __init__(self, message):
        super().__init__(self, message)
        self.message = message

    def __str__(self):
        return f"{self.message}"