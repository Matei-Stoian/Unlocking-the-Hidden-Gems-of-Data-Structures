class FenwickTree:
    def __init__(self, n: int):
        """
        Initialize a Fenwick Tree(Binary Indexed Tree) with 'n' elements.

        Parameters:
            n (int): Size of the array.
        """
        self.tree = [0] * (n + 1)
        self.size = n

    def update(self, index: int, delta: int):
        """
        Update the Fenwick Tree with a delta at a specific index.

        Parameters:
            index (int): The index to update.
            delta (int): The value to add at the index.
        """

        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Computes the least valuable bit(lsb)

    def query(self, index: int) -> int:
        """
        Compute the prefix sum from the start to the given index.

        Parameters:
            index (int): The index to compute the prefix sum up to.

        Return:
            (int): The computed sum.
        """

        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_query(self, left: int, right: int) -> int:
        """
        Get the sum of the range [left, right] (1-indexed).

        Parameters:
            left (int): The starting index of the range.
            right (int): The ending index of the range.

        Returns:
            (int): The sum from left to right (inclusive).

        """
        return self.query(right) - self.query(left - 1)


if __name__ == "__main__":
    fenwick_tree = FenwickTree(5)

    initial_values = [0, 1, 2, 3, 4, 5]
    for i in range(1, len(initial_values)):
        fenwick_tree.update(i, initial_values[i])

    print(
        "Sum of first 3 elements (1 to 3):", fenwick_tree.query(3)
    )  # Output: 6 (1 + 2 + 3)

    fenwick_tree.update(2, 3)  # Update index 2 with delta 3

    print(
        "Sum of first 3 elements after update:", fenwick_tree.query(3)
    )  # Output: 9 (1 + 5 + 3)

    print(
        "Sum from index 2 to 4:", fenwick_tree.range_query(2, 4)
    )  # Output: 12 (5 + 3 + 4)
