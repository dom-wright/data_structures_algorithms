'''
Splay trees

Splay trees are a variant of binary search tree (BST) whose goal is to keep the tree as balanced as possible following operations on the tree, such as search, insertion, and deletion. The mechanism in which splay trees try to stay balanced is by moving nodes to the root of the tree (splaying) after they are accessed by any operation. For trees that are frequented by search operations, this will help keep more frequently accessed nodes near the top of the tree, thus reducing the average time needed to access those nodes.

Use cases:
Splay trees will be useful anywhere where there is a mismatch of access to parts of data and clear patterns which can make access quicker.
- Caching: store frequently accessed data
- Data Compression: Splay trees have been used in certain data compression algorithms, such as the Dynamic Huffman coding
- File Systems: Splay trees can be utilised in file systems to improve the performance of file access e.g. last accessed files/directories.

Runtime:
Splay trees are useful tree implementations when the use case requires more lookups than insertion and deletion operations. if the distribution of lookup values is even, the tree does a good job of staying balanced, and we can rely on O log(n) runtime. if they aren't even, more frequent values will at least stay near the top of the tree. although good balance isn't guaranteed, which can lead to worse performance than O(n).
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, original_parent):
        # Switch child pointers
        target_node = original_parent.left
        target_node.parent = original_parent.parent

        # Right child of target node, becomes left child of original parent now
        original_parent.left = None
        if target_node.right != None:
            original_parent.left = target_node.right
            target_node.right.parent = original_parent

        # Set target nodes new parent, if none, it's the root
        if target_node.parent == None:
            self.root = target_node

        elif original_parent == original_parent.parent.right:
            original_parent.parent.right = target_node
        else:
            original_parent.parent.left = target_node

        # original parent becomes right child of target
        target_node.right = original_parent
        original_parent.parent = target_node

    def _left_rotate(self, original_parent):
        # Switch child pointers
        target_node = original_parent.right
        target_node.parent = original_parent.parent

        # Left child of target node, becomes right child of original parent now
        original_parent.right = None
        if target_node.left != None:
            original_parent.right = target_node.left
            target_node.left.parent = original_parent

        # Set target nodes new parent, if none, it's the root
        if target_node.parent == None:
            self.root = target_node

        elif original_parent == original_parent.parent.left:
            original_parent.parent.left = target_node
        else:
            original_parent.parent.right = target_node

        # original parent becomes right child of target
        target_node.left = original_parent
        original_parent.parent = target_node

    def _zig(self, node):
        self._right_rotate(node.parent)

    def _zag(self, node):
        self._left_rotate(node.parent)

    def _zig_zig(self, node):
        self._right_rotate(node.parent.parent)
        self._right_rotate(node.parent)

    def _zag_zag(self, node):
        self._left_rotate(node.parent.parent)
        self._left_rotate(node.parent)

    def _zig_zag(self, node):
        self._left_rotate(node.parent)
        self._right_rotate(node.parent)

    def _zag_zig(self, node):
        self._right_rotate(node.parent)
        self._left_rotate(node.parent)

    def splay(self, node):
        if node == self.root or node.parent == None:
            return

        while node != self.root:
            parent = node.parent

            if parent == self.root:
                if parent.left == node:
                    self._zig(node)
                else:
                    self._zag(node)
                self.root = node

            else:
                grandparent = parent.parent
                if parent.left == node:
                    if grandparent.left == parent:
                        self._zig_zig(node)
                    else:
                        self._zag_zig(node)
                else:
                    if grandparent.left == parent:
                        self._zig_zag(node)
                    else:
                        self._zag_zag(node)

            if node.parent == None:
                self.root = node

    def search(self, value, node=None):
        if node is None:
            node = self.root

        if node.value == value:
            self.splay(node)
            return self.root

        elif value < node.value:
            return self.search(value, node.left)
        else:
            return self.search(value, node.right)

    def insert(self, value):
        new_node = Node(value)

        current_node = self.root
        if current_node is None:
            self.root = new_node
            return

        last_parent = None
        while current_node is not None and current_node.value != new_node.value:
            last_parent = current_node
            if new_node.value <= current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node.parent = last_parent
        if new_node.value < last_parent.value:
            last_parent.left = new_node
        elif new_node.value > last_parent.value:
            last_parent.right = new_node

        self.splay(new_node)

    def _find_max_node(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, value):
        # Find target node to delete
        node = self.root
        while node != None and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right

        if node is None:
            return

        # Splay first
        self.splay(node)

        # Split tree into two, removing reference to root as parent for the first left/right child
        if node.right is None and node.left is None:
            self.root = None
            return
        elif node.left is None:
            node.right.parent = None
            return node.right
        elif node.right is None:
            node.left.parent = None
            return node.left
        else:
            left_side_tree = node.left
            left_side_tree.parent = None

            right_side_tree = node.right
            right_side_tree.parent = None

            new_root = self._find_max_node(left_side_tree)

            self.splay(new_root)

            new_root.right = right_side_tree
            right_side_tree.parent = new_root
            self.root = new_root
