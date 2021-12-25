import itertools
from os import remove

class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

    def display(self):
        lines, *_ = self._display_aux()

        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.negative_child is None and self.positive_child is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only positive_child child.
        if self.negative_child is None:
            lines, n, p, x = self.positive_child._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only negative_child child.
        if self.positive_child is None:
            lines, n, p, x = self.negative_child._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        positive_child, n, p, x = self.positive_child._display_aux()
        negative_child, m, q, y = self.negative_child._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            positive_child += [n * ' '] * (q - p)
        elif q < p:
            negative_child += [m * ' '] * (p - q)
        zipped_lines = zip(positive_child, negative_child)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms

    def __str__(self):
        return self.illness + " for " + str(self.symptoms)
        
class Diagnoser:
    def __init__(self, root: Node):
        self.root = root
        
    def diagnose(self, symptoms):
        return self.helper(self.root, symptoms)
    
    def helper(self, node, symptoms):
        if not node.positive_child and not node.negative_child:
            return node.data

        if node == None:
            return None

        if node.data in symptoms:
            return self.helper(node.positive_child, symptoms)
        
        return self.helper(node.negative_child, symptoms)


if __name__ == "__main__":
    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)
    diagnoser = Diagnoser(root)

    diagnoser.root.display()

    assert "cold" == diagnoser.diagnose(["cough"])