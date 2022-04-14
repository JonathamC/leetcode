# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newLIST = ListNode()
        head = newLIST
        while list1 and list2: 
            if list1.val <= list2.val: 
                newLIST.next = list1
                newLIST = newLIST.next
                list1 = list1.next 
                
            else: 
                newLIST.next = list2 
                newLIST = newLIST.next
                list2 = list2.next
                
        while list1: 
            newLIST.next = list1
            newLIST = newLIST.next
            list1 = list1.next
        
        while list2: 
            newLIST.next = list2 
            newLIST = newLIST.next
            list2 = list2.next 
        
        return head.next