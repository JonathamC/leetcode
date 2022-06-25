class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None 
        current = head 
        duplicate = []
        while current: 
            if current.val not in duplicate: 
                duplicate.append(current.val)
                previous = current 
                current = current.next 
                
            else: 
                
                previous.next = current.next 
                current = current.next 
                
        
        return head

lst = ListNode(1)
lst.next = ListNode(1)
print(lst)