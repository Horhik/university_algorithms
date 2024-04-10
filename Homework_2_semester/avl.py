import matplotlib.pyplot as plt

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self.fig, self.ax = plt.subplots()

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is not None:
            node.height = max(self.height(node.left), self.height(node.right)) + 1

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def rebalance(self, node):
        self.update_height(node)
        balance_factor = self.balance(node)

        if balance_factor > 1:
            if self.balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance_factor < -1:
            if self.balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, node, key):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        self.update_height(node)
        node = self.rebalance(node)
        self.update_visualization()

        return node

    def remove(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.remove(node.left, key)
        elif key > node.key:
            node.right = self.remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.find_min(node.right)
            node.key = temp.key
            node.right = self.remove(node.right, temp.key)

        self.update_height(node)
        node = self.rebalance(node)
        self.update_visualization()

        return node

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    def draw_tree(self, node, x=0, y=0, spacing=1):
        if node is not None:
            self.ax.text(x, y, str(node.key), bbox=dict(facecolor='white', alpha=0.5), horizontalalignment='center')
            if node.left:
                self.ax.plot([x, x - spacing], [y, y - 1], 'k-')
                self.draw_tree(node.left, x - spacing, y - 1, spacing / 2)
            if node.right:
                self.ax.plot([x, x + spacing], [y, y - 1], 'k-')
                self.draw_tree(node.right, x + spacing, y - 1, spacing / 2)

    def update_visualization(self):
        self.ax.clear()
        self.draw_tree(self.root)
        self.ax.axis('off')
        plt.pause(0.5)  # Adjust pause duration as needed
        plt.show(block=False)

    def visualize_tree(self):
        self.draw_tree(self.root)
        self.ax.axis('off')
        plt.show()

# Example usage:
avl_tree = AVLTree()
avl_tree.root = avl_tree.insert(avl_tree.root, 1)
avl_tree.root = avl_tree.insert(avl_tree.root, 2)
avl_tree.root = avl_tree.insert(avl_tree.root, 3)
avl_tree.root = avl_tree.insert(avl_tree.root, 4)
avl_tree.root = avl_tree.insert(avl_tree.root, 5)
avl_tree.root = avl_tree.insert(avl_tree.root, 7)
avl_tree.root = avl_tree.insert(avl_tree.root, 8)
avl_tree.root = avl_tree.insert(avl_tree.root, 9)
avl_tree.root = avl_tree.insert(avl_tree.root, 10)
avl_tree.root = avl_tree.insert(avl_tree.root, 11)
avl_tree.root = avl_tree.insert(avl_tree.root, 12)


avl_tree.visualize_tree()
