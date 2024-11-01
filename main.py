# Define the Node class
class Node:
    def __init__(self, data, value):
        self.data = data  # Store the data for the node
        self.next = None  # Initialize the next pointer to None (no next node yet)
        self.value = value # Exercise 3
        self.left = None # Exercise 3
        self.right = None # Exercise 3

# Create individual nodes with data values
node1 = Node(10)  # First node with data 10
node2 = Node(28)  # Second node with data 20
node3 = Node(30)  # Third node with data 30
node4 = Node(31)  # Exercise 2

# Link the nodes together to form a chain (a simple linked list)
def create_linked_list(values):
    head = None
    current = None

    for value in values:
        new_node = Node(value)
        if head is None:
            head = new_node
            current = new_node
            
        else:
            current.next = new_node
            current = new_node

    return head
# Link node1 to node2
node1.next = node2
# Link node2 to node3
node2.next = node3
#Exercise 2
node3.next = node4

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
# Function to traverse the list and print each node's data
def print_linked_list(head):
# Start with the head node
    current = head
# Continue until reach the end of the list (None)
    while current:
# Print the data and follow with "->"
        print(current.data, end = " -> ")
# Move to the next node in the list
        current = current.next
# Indicate the end of the list
if __name__ == '__main__':
    llist = LinkedList
    llist.head = node1
    second = node2
    third = node3
    fourth = node4

    llist.head.next = second
    second.next = third
    third.next = fourth

llist = LinkedList()
# Test the print function by printing the linked list from node1
print_linked_list(node1)

# Exercise 1: Update node2's data and print the list again
# Change data in the second node

# Exercise 2: Add a new node (node4) with a new value and link it to the list
# Create a new fourth node with data 40
# Link node3 to the new node4

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
# Exercise 3: Modify the print function to count nodes and print the count
def print_linked_list_with_count(head):
    # Start with the head node
    # Initialize a counter for the nodes
    count = count_nodes(head)
    # Traverse until the end of the list
    # Print the data for each node
    print("Numbr of Nodes: ", count)
    # Move to the next node
    # Increment the count for each node visited
    # Indicate the end of the list
    # Print the total node count

# Test the new function to print the list and count nodes
