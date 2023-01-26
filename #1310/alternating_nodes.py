class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def rearrange_list(head: Node) -> Node:
    current = head
    while current and current.next:
        current.data, current.next.data = current.next.data, current.data
        current = current.next.next
    return head

# Create the linked list 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

if __name__ == '__main__':
    # Rearrange the linked list
    new_head = rearrange_list(head)

    # Print the rearranged linked list
    current_node = new_head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next
