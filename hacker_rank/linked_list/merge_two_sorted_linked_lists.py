# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    dummy_head = SinglyLinkedListNode(0)
    current = dummy_head
    while(head1 != None and head2 != None):
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current = current.next

    if(head1 == None):
        current.next = head2
    else:
        current.next = head1
        
    return dummy_head.next

            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()

    # Time Complexity: O(n + m) -> n = len(head1) | m = len(head2)
    # Space Complexity: O(1)
    # Reference for the solution: https://www.youtube.com/watch?v=GfRQvf7MB3k
