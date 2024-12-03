class TrieNode:
    def __init__(self):
        """Initialize a node in the Trie.
        Each node contains a dictionary of child nodes and a boolean flag to indicate the end of a word.
        """
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        """Initialize the root of the Trie."""
        self.root = TrieNode()

    def insert(self, word: str):
        """
        Insert a word in the Trie.

        Parameters
            word (str): The word to insert into the Trie.
        """

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        Parameters:
            word (str): The word to search for in the Trie.

        Return:
            bool: True if the word is in the Trie, otherwise False.
        """

        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> list[str]:
        """
        Return all words in the Trie that start with the given prefix.

        Parameters:
            prefix (str): The prefix to search for

        Return:
            list: A list of words that start with the given prefix.
        """

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return self._helper(node, prefix)

    def _helper(self, node: TrieNode, prefix: str) -> list[str]:
        """
        Collect all words starting from a given node using an iterative DFS approach for better performance.

        Parameters:
            node (TrieNode): The current Trie node.
            prefix (str): The current prefix of the word being built.

        Return:
            list: List of words starting with the prefix.
        """

        words = []
        stack = [(node, prefix)]

        while stack:
            current_node, current_prefix = stack.pop()

            if current_node.is_end_of_word:
                words.append(current_prefix)

            for char, child_node in current_node.children.items():
                stack.append((child_node, prefix + char))

        return words


if __name__ == "__main__":
    trie = Trie()

    print("Inserting words: 'apple', 'app', 'apricot', 'banana', 'bat', 'batman'")
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apricot")
    trie.insert("banana")
    trie.insert("bat")
    trie.insert("batman")

    print("\nSearch Tests:")
    print("Search for 'apple':", trie.search("apple"))  # Expected: True
    print("Search for 'app':", trie.search("app"))  # Expected: True
    print("Search for 'apricot':", trie.search("apricot"))  # Expected: True
    print("Search for 'banana':", trie.search("banana"))  # Expected: True
    print("Search for 'batman':", trie.search("batman"))  # Expected: True
    print("Search for 'bat':", trie.search("bat"))  # Expected: True
    print("Search for 'ap':", trie.search("ap"))  # Expected: False (not a full word)
    print(
        "Search for 'bananaa':", trie.search("bananaa")
    )  # Expected: False (not in Trie)

    print("\nStarts_with Tests:")
    print(
        "Words that start with 'app':", trie.starts_with("app")
    )  # Expected: ['apple', 'app']
    print(
        "Words that start with 'ba':", trie.starts_with("ba")
    )  # Expected: ['banana', 'bat', 'batman']
    print(
        "Words that start with 'bat':", trie.starts_with("bat")
    )  # Expected: ['bat', 'batman']
    print(
        "Words that start with 'apri':", trie.starts_with("apri")
    )  # Expected: ['apricot']
    print(
        "Words that start with 'bats':", trie.starts_with("bats")
    )  # Expected: [] (no such prefix)
    print(
        "Words that start with '':", trie.starts_with("")
    )  # Expected: All inserted words
