import random


class SkipNode:
    """
    A SkipList Node
    """
    def __init__(self, value, level):
        """
        Initialize a skip list node.
        Parameters:
            value (int): The integer value to store in the node.
            level (int): The level of the node (how many next pointers it will have).
        """
        self.value = value
        self.next = [None] * (level + 1)


class SkipList:
    def __init__(self, max_level):
        """
        Initialize the skip list.
        
        Parameters:
            max_level (int): The maximum number of levels in the skip list.
        """
        self.maxLevel = max_level
        self.head = SkipNode(None, max_level)  
        self.level = 0
        self.size = 0

    def __len__(self):
        return self.size

    def random_level(self):
        """
        Generate a random level for the new node.
        
        Returns:
            int: The level of the new node (randomly generated).
        """
        level = 0
        while random.random() < 0.5 and level < self.maxLevel:
            level += 1
        return level

    def insert(self, value):
        """
        Insert an integer value into the skip list.
        
        Parameters:
            value (int): The integer value to insert.
        """
        update = [None] * (self.maxLevel + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].value < value:
                current = current.next[i]
            update[i] = current

        current = current.next[0]

        if current is None or current.value != value:
            new_level = self.random_level()
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.head
                self.level = new_level

            new_node = SkipNode(value, new_level)

            for i in range(new_level + 1):
                new_node.next[i] = update[i].next[i]
                update[i].next[i] = new_node

            self.size += 1

    def search(self, value):
        """
        Search for an integer value in the skip list.

        Parameters:
            value (int): The integer value to search for.

        Return:
            bool: True if the value is found, False otherwise.
        """
        current = self.head

        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].value < value:
                current = current.next[i]
        current = current.next[0]

        return current is not None and current.value == value

    def delete(self, value):
        """
        Delete an integer value from the skip list.
        
        Parameters:
            value (int): The integer value to delete.
        """
        update = [None] * (self.maxLevel + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].value < value:
                current = current.next[i]
            update[i] = current

        current = current.next[0]

        if current and current.value == value:
            for i in range(self.level, -1, -1):
                if update[i].next[i] == current:
                    update[i].next[i] = current.next[i]

            while self.level > 0 and self.head.next[self.level] is None:
                self.level -= 1

            self.size -= 1



if __name__ == '__main__':
    # Example Usage
    skip_list = SkipList(4)

    # Inserting integer values into the skip list
    skip_list.insert(10)
    skip_list.insert(20)
    skip_list.insert(15)
    skip_list.insert(5)

    # Check the length of the skip list
    print("Skip List size:", len(skip_list))  # Output: 4

    # Deleting a value
    skip_list.delete(10)
    print("Skip List size after deletion:", len(skip_list))  # Output: 3
