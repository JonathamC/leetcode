class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def deleteDuplicates(self, head):
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


def printList(head): 
    string = "["
    while (head): 
        string += "{}, ".format(head.val)
        head = head.next
    
    string = string[:-2] + "]"
    print(string)


        

lst = ListNode(1)
lst.next = ListNode(1)
lst.next.next = ListNode(2)
lst.next.next.next = ListNode(3)
printList(lst)
lst.deleteDuplicates(lst)
printList(lst)