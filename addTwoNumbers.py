class ListNode: 

    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

    def print_list(ll): 
        s = "["
        while ll: 
            s += str(ll.val) + ","
            ll = ll.next 
        
        print(s[:-1]+ "]")


def addTwoNumbers(l1, l2):
    ans = ListNode()
    curr = ans
    
    overflow = 0
    while l1 and l2: 
        cal = l1.val + l2.val + overflow
        if cal > 9: 
            overflow = 1 
            curr.next = ListNode(cal % 10)
            curr = curr.next
            
        else: 
            overflow = 0
            curr.next = ListNode(cal)
            curr = curr.next
        
        l1 = l1.next 
        l2 = l2.next 
    while l1: 
        cal = l1.val + overflow 
        if cal > 9: 
            curr.next = ListNode(cal % 10)
            curr = curr.next
            overflow = 1 
        else: 
            overflow = 0 
            curr.next = ListNode(cal)
            curr = curr.next
        
        l1 = l1.next 
        
    while l2: 
        cal = l2.val + overflow 
        if cal > 9: 
            curr.next = ListNode(cal % 10)
            curr = curr.next
            overflow = 1 
        else: 
            overflow = 0 
            curr.next = ListNode(cal)
            curr = curr.next
        
        l2 = l2.next 
    
    if overflow == 1: 
        curr.next = ListNode(1)
        curr = curr.next


    return ans.next
    
ll1 = ListNode(0)
l1 = ll1
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(4)
l1 = l1.next 
l1.next = ListNode(3)
l1 = l1.next 

ListNode.print_list(ll1.next)

ll2 = ListNode(0)
l2 = ll2 
l2.next = ListNode(5)
l2 = l2.next
l2.next = ListNode(6)
l2 = l2.next 
l2.next = ListNode(4)
l2 = l2.next 

ListNode.print_list(ll2.next)

ListNode.print_list(addTwoNumbers(ll1, ll2).next)