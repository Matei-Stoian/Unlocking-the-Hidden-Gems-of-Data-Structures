class Node:

    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None


    def __repr__(self):
        return f"Node({self.key})"
    

class SplayTree:

    def __init__(self):
        self.root = None

    def _right_rotate(self,x:Node):
        """
        Apply the right rotate function at node x.
        """
        y:Node = x.left
        x.left = y.right
        y.right = x
        return y
    
    def _left_rotate(self,x:Node):
        """
        Apply the left rotate function at node x.
        """
        y:Node = x.right
        x.right = y.left
        y.left = x
        return y
    
    def _splay(self,root,key):
        """
        Bring the node with the given key to the root of the subtree rooted at 'root' by using the zig or zag move or the combination of two.
        If the key is not found, bring the last accessed node to the root.
        """

        if root is None or root.key == key:
            return root
        
        # The key is in the left subtree
        if root.key > key:
            if root.left is None:
                return root #Key not found
            
            #Zig-Zig(left-left)
            if root.left.key > key:
                root.left.left = self._splay(root.left.left,key)
                root = self._right_rotate(root)

            #Zig-Zag(left-right)
            elif root.left.key < key:
                root.left.right = self._splay(root.left.right,key)
                if root.left.right is not None:
                    root.left = self._left_rotate(root.left)
            return root if root.left is None else self._right_rotate(root)


        # The key is in the right subtree
        else:
            if root.right is None:
                return root

            #Zag-Zig(right-left)
            if root.right.key > key:
                root.right.left = self._splay(root.right.left,key)
                if root.right.left is not None:
                    root.right = self._right_rotate(root.right)
            #Zag-Zag(right-right)
            elif root.right.key < key:
                root.right.right = self._splay(root.right.right,key)
                root = self._left_rotate(root)
            return root if root.right is None else self._left_rotate(root)
    
    def insert(self,key):
        """
        Insert a new key into the tree.
        """
        if self.root is None:
            self.root = Node(key)
            return
        
        self.root = self._splay(self.root,key)
        
        if self.root.key == key:
            print(f"Key {key} is allready in the tree.")
            return
        
        new_node = Node(key)

        if self.root.key > key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node


    def delete(self,key):
        if self.root is None:
            print("Tree is empty.")
            return 

        self.root = self._splay(self.root,key)

        if self.root.key != key:
            print(f"Key {key} not found.")
            return 
        
        if self.root.left is None:
            self.root = self.root.right
        else:
            temp = self.root.right
            self.root = self._splay(self.root.left,key)
            self.root.right = temp
        
    def search(self,key):
        self.root = self._splay(self.root,key)
        found  = self.root is not None and self.root.key == key
        print(f"{'Found' if found else 'Did not found'} {key}.")
        return found
    
    def inorder_traversal(self):

        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.key,end=" ")
                _inorder(node.right)
        
        _inorder(self.root)
        print()

if __name__ == '__main__':
    # Example usage
    tree = SplayTree()

    print("Initial Insertions:")
    # Insert elements
    tree.insert(10)
    tree.insert(20)
    tree.insert(5)
    tree.insert(15)
    tree.insert(25)

    # In-order traversal after initial insertions
    print("In-order traversal after initial insertions:")
    tree.inorder_traversal()

    print("\nSearching for an Existing Element:")
    # Search for an element that exists
    tree.search(15)  # This should splay 15 to the root

    print("\nIn-order traversal after searching for 15:")
    tree.inorder_traversal()

    print("\nSearching for a Non-Existent Element:")
    # Search for an element that doesn’t exist
    tree.search(30)  # This should bring the closest accessed node to the root

    print("\nIn-order traversal after searching for 30 (non-existent):")
    tree.inorder_traversal()

    print("\nAttempting to Insert a Duplicate:")
    # Attempt to insert a duplicate element
    tree.insert(15)  # Since 15 already exists, no new insertion should occur

    print("\nIn-order traversal after attempting to insert duplicate 15:")
    tree.inorder_traversal()

    print("\nDeleting Elements:")
    # Delete an element that exists
    tree.delete(10)  # This should remove 10 from the tree

    print("\nIn-order traversal after deleting 10:")
    tree.inorder_traversal()

    # Delete an element that doesn’t exist
    tree.delete(30)  # This should not change the tree

    print("\nIn-order traversal after attempting to delete 30 (non-existent):")
    tree.inorder_traversal()

    # Delete the root element
    print("\nDeleting the Root Element (current root):")
    if tree.root is not None:
        tree.delete(tree.root.key)  # Delete current root, which is 25 if no prior splay

    print("\nIn-order traversal after deleting the current root:")
    tree.inorder_traversal()

    print("\nTesting Edge Case with Empty Tree:")
    # Testing on an empty tree
    empty_tree = SplayTree()

    # Attempt to delete on an empty tree
    empty_tree.delete(5)

    # Attempt to search in an empty tree
    empty_tree.search(5)

    print("In-order traversal of empty tree:")
    empty_tree.inorder_traversal()
