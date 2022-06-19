class Node:
    def __init__(self, value: int = 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def sum_left_and_right(self):
        left_summa, right_summa = 0, 0
        if self.left:
            left_summa += self.left.sum_left_and_right()
        if self.right:
            right_summa += self.right.sum_left_and_right()
        return max(left_summa, right_summa) + self.value


if __name__ == '__main__':
    binary_tree = Node(1, Node(2, Node(1, Node(9)), Node(7)), Node(9, Node(5, Node(7)), Node(2)))
    print(binary_tree.sum_left_and_right())


