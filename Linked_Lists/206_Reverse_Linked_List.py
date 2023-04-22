def reverseList(head):
    prev, curr = None, head
    # reversing the links of the list

    while curr:
        # temp
        nxt = curr.next

        # second value is going to become new prev
        curr.next = prev
        # shift pointer across,
        prev = curr
        curr = nxt
    #prev pointer is equal to the new head
    return prev

def reverseList_recursive(self, head):
    if not head: #if
        return None

    newHead = head

    if head.next:
        newHead = self.reverseList_recursive(head.next)
        head.next.next = head
    head.next = None
    return newHead

    # head = (1) head.next = None, so no change
  """
  Head = (1,2)
  NewHead = (1,2)
  head.next = 2
    newHead = reverselist(2)
        head.next = None
        head.next = None
        head(1 -> 2 -> None)
...

    Don't understand the recursive function, ask Nicky?
    
        
  
  """