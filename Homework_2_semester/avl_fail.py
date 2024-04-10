#!/usr/bin/env python3
#
import matplotlib.pyplot as plt

def node_height(node):
    if (node == None):
        return 0
    return node.height

def balance_height(node):
        if node == None:
            return 0

        hl = node_height(node.left)
        hr = node_height(node.right)

        return max(hl, hr) + 1



def height_or_zero(node):
    if node == None:
        return 0
    return balance_height(node)



class Node:

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1

    def turn_into(self, frog):
        self.key = frog.key
        self.left = frog.left
        self.right = frog.right
        self.height = frog.height

    def copy():
        return Node(key=self.key, left=self.left, right=self.right)

    def bfactor(self):
        return node_height(self.right) - node_height(self.left)


    def rotate_right(self):
        x = self.left
        self.left = x.right

        x.right.__dict__.update(self.__dict__)
        x.right.height = balance_height(x.right)
        x.left.height = balance_height(x.right)

        x.height = balance_height(x)

        self.__dict__.update(self.__dict__)


    def rotate_left(self):


        x = self.right

        self.right = x.left

        x.left=Node()
        x.left.__dict__.update(self.__dict__)

        x.right.height = balance_height(x.right)
        x.left.height = balance_height(x.right)

        x.height = balance_height(x)


        self.__dict__.update(x.__dict__)
    def balance(self):

        self.height = balance_height(self)
        print("balancing height", self.height)

        bf = self.bfactor()
        # if right subtree is higher than left
        if bf == 2:
            print("R > L")
            # if left branch (left subtree of the right subtree) are higher
            if self.right.bfactor() < 0:
                # this making right branch higher than left
                self.right.rotate_right()
            # anyway rotating right subree
            # in any case now right subtree is balanced, but steel higher than left
            self.rotate_left()
        # same as for right, but if left subtree is hegher than right
        if bf == -2:
            print("R < L")
            if self.left.bfactor() > 0 :
                self.left.rotate_left
            self.rotate_rigth()

    def repair_node(self, side):
        if side == 'left':
            if self.left == None:
                self.left = Node()

        if side == 'right':
            if self.right == None:
                self.right = Node()

    def repair_height(self, key, h=1):

        print(f'depth: {h}/{self.height}--key: {self.key}--goal: {key}\n')

        if key == self.key:
            print('Goal depth: ', h)
            return h

        if key < self.key:

            total_height = self.left.repair_height(key, h=h+1)
            curr_height = total_height - h

            self.height = max(curr_height, node_height(self.right)) + 1

            return self.height

        if key > self.key:
            total_height = self.right.repair_height(key, h=h+1)
            curr_height = total_height - h

            print(curr_height, '<- l r ->', node_height(self.right), f'{total_height} - {h}')
            self.height = max(curr_height , node_height(self.left)) + 1

            return total_height

    def _insert(self, key):
        #print("inserting key ", key, "into self", self.right, " ", self.left)
        if self.key == None:
            self.key = key
            self.height = 1


        if key < self.key:
            #print("key is smaller than ", self.key)
            self.repair_node('left')
            self.left._insert(key)

        elif key > self.key:
            #print("key is larger than ", self.key)
            self.repair_node('right')
            self.right._insert(key)

    def insert(self, key):
        self._insert(key)
        print('-----------------')
        self.repair_height(key)
        self.balance()
        self.draw_tree()
        self.update()



    def find(self, key):

        if self.key == key:
            return self
        if key < self.key:
            if self.left == None:
                return None
            self.left.find(key)

        elif key > self.key:
            if self.right == None:
                return None
            self.right.find(key)

    def findmin(self):
        if self.left == None:
            return self.key

        return self.left.findmin()

    def remove_hard(self, key):
        pass

    def replace(self, key, node):

        if self.key == key:
            self = node
            return True

        elif key < self.key:
            return self.left.replace(key, node)

        elif key > self.key:
            return self.right.replace(key, node)



    def remove(self, key):
        node = self.find(key)

        if node != None:
            if node.right != None:

                min_key = node.right.findmin()
                min_node = self.find(min_key)
                mnr = min_node.right

                min_node.right = node.right
                min_node.left = node.left

                node = min_node

                node.remove(min_key)

            elif node.left != None:
                node = node.left
            else:
                node = None

            node.balance()
            self.replace(key, node)
            self.balance()


    def draw_tree(self, x=0, y=0, spacing=1):
        if self is not None:
            plt.text(x, y, str(self.key) + ' ' + str(self.height), bbox=dict(facecolor='white', alpha=0.5), horizontalalignment='center')
            if self.left:
                plt.plot([x, x - spacing], [y, y - 1], 'k-')
                self.left.draw_tree(x - spacing, y - 1, spacing / 2)
            if self.right:
                plt.plot([x, x + spacing], [y, y - 1], 'k-')
                self.right.draw_tree(x + spacing, y - 1, spacing / 2)

    def update(self):
        plt.clf()  # Clear current figure
        self.draw_tree()  # Draw the updated tree
        plt.show()  # Show the updated tree

def plot_tree(node, x=0, y=0, spacing=20, ax=None):
    fig = None
    if ax is None:
        fig, ax = plt.subplots()
    if node is not None:
        ax.plot(x, y, 'o', markersize=16, color='black')  # plot current node
        ax.text(x, y, str(node.key) + ' ' + str(node.height), ha='center', va='center', color='pink')  # add node key as text
        if node.left is not None:
            ax.plot([x, x - spacing], [y, y - spacing], '-k')  # plot left child edge
            plot_tree(node.left, x - spacing, y - spacing, spacing, ax=ax)  # recursively plot left subtree
        if node.right is not None:
            ax.plot([x, x + spacing], [y, y - spacing], '-k')  # plot right child edge
            plot_tree(node.right, x + spacing, y - spacing, spacing, ax=ax)  # recursively plot right subtree
    return fig


root = Node()

root.insert(1)


print(root.left , root.right)
root.insert(2)
print(root.left , root.right)
root.insert(3)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(8)
root.insert(9)
root.insert(10)
root.insert(11)
root.insert(11)
root.insert(12)
root.insert(13)
root.insert(14)
root.insert(15)
root.insert(16)
root.insert(17)
root.insert(18)

