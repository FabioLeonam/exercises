# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    # Case 1: empty list
    if head == None:
        head = new_node
        return head
    #Case 2: Insert at head
    elif head.data > data:
            head.prev = new_node
            new_node.next = head
            head = new_node
            return head
    else:
        pointer = head
        while(pointer.data < data):
            #Case 3: Insert at tail
            if pointer.next == None:
                pointer.next = new_node
                new_node.prev = pointer
                return head
            else:
                pointer = pointer.next

        # Case 4: Insert at somewhere middle
        pointer.prev.next = new_node
        new_node.prev = pointer.prev
        pointer.prev = new_node
        new_node.next = pointer
        return head
        
             
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()