class MarbleBag:
    """
    Simulates a bag of marbles where colored marbles can 
    be added or randomly withdrawn.
    """

    def __init__(self, size):
        """
        Create an empty marble bag.

        :param size: (int) The maximum number of marbles the bag can contain, 
            if set to zero the bag can contain any number of marbles.
        """
        pass


    def add(self, color):
        """
        Add a colored marble to the bag.

        :param color: (string) The name of the color of the marble.
        """
        pass


    def take(self):
        """
        Randomly retrieve a marble from the bag. 
        The selected marble is removed from the bag.

        :return: (string) The color of the retrieved marble.
        """
        pass


    def peek(self):
        """
        Randomly look at a marble from the bag. 
        The selected marble is put back in the bag.

        :return: (string) The color of the selected marble
        """
        pass
