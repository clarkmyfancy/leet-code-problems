
class Node:
    def __init__(self, x):
        self.val = x 
        self.next = None

def main():
    n1 = Node(2)
    n2 = Node(4)
    n3 = Node(3)
    n1.next = n2 
    n2.next = n3

    n4 = Node(5)
    n5 = Node(6)
    n6 = Node(4)
    n4.next = n5 
    n5.next = n6
    
    sum1 = extract_number_from_list(n1)
    sum2 = extract_number_from_list(n4)

    total = sum1 + sum2

    head_node = extract_list_from_number(total)

    print_list(head_node)

def extract_number_from_list(node):
    currentNode = node
    multiplier = 1
    sum = multiplier * currentNode.val 
    while currentNode.next != None:
        currentNode = currentNode.next
        multiplier *= 10
        sum += multiplier*currentNode.val
    return sum

def extract_list_from_number(total):
    list_of_nodes = []
    num_digits = get_num_digits(total)
    total_as_str = str(total)
    for _ in range(num_digits):
        if len(total_as_str) == 0:
            break
        y = total_as_str[0]
        total_as_str = total_as_str[1:]
        new_int = int(y)
        list_of_nodes.append(Node(new_int))
    x = 0
    list_of_nodes = list_of_nodes[::-1]
    while x < num_digits - 1:
        list_of_nodes[x].next = list_of_nodes[x + 1]
        x += 1
    if not list_of_nodes:
        return Node(0)
    if list_of_nodes[0]:
        return list_of_nodes[0]

def get_num_digits(total):
    x = total 
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count

def print_list(head_node):
    curr_node = head_node
    print(curr_node.val)
    while curr_node.next != None:
        curr_node = curr_node.next
        print(curr_node.val)

if __name__ == "__main__":
    main()