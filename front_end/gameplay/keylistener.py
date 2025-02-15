class KeyListener:
    def __init__(self):
        """
        Initializes the KeyListener with an empty list to track pressed keys.
        """
        self.keys: list[int] = []  # List to store currently pressed keys

    def add_key(self, key: int) -> None:
        """
        Adds a key to the list if it's not already present.
        
        :param key: The keycode of the pressed key.
        """
        if key not in self.keys:
            self.keys.append(key)

    def remove_key(self, key: int) -> None:
        """
        Removes a key from the list if it exists.
        
        :param key: The keycode of the released key.
        """
        if key in self.keys:
            self.keys.remove(key)

    def key_pressed(self, key: int) -> bool:
        """
        Checks if a key is currently pressed.
        
        :param key: The keycode to check.
        :return: True if the key is in the list, False otherwise.
        """
        return key in self.keys

    def clear(self) -> None:
        """
        Clears the list of pressed keys.
        """
        self.keys.clear()
