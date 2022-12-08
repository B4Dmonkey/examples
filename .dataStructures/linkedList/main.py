#
# * Check note book for usage
class Node:
    def __init__(self, data):
        self.data = data    # * Data stored at this index
        self.next = None    # * Pointer to the next item on the list
        # self.prev = None  # * When making a doubled linked list make sure to include previous

    # * Helper function to show the list
    def __str__(self):
        return f"Node: <data: { self.data }\tnext: Node({ self.next.data if self.next else None })>"


class LinkedList:
    def __init__(self, node=None):
        self.nodes = node

    def __str__(self):
        string_rep = ""
        nodes = self.nodes
        count = 0

        while nodes:
            string_rep += f"{ count }:\t{ nodes }\n"
            nodes = nodes.next
            count += 1

        return string_rep

    def length(self):
        nodes = self.nodes
        count = 0
        while nodes:
            count += 1
            nodes = nodes.next
        return count

    def insert(self, node):
        node.next = self.nodes
        self.nodes = node
        return self.nodes

    def search(self, data):
        nodes = self.nodes
        while nodes:
            if nodes.data == data:
                return nodes
            nodes = nodes.next
        return nodes

    def delete(self, data):
        node_found = self.search(data)
        if node_found:
            nodes = self.nodes
            while nodes:
                if nodes.next.data == node_found.data:
                    nodes.next = node_found.next
                    return nodes
                nodes = nodes.next
        return False


if __name__ == '__main__':
    pass
