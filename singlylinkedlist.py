class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    # def traverse(self):
    #     a=self
    #     print("Traversing the list...")
    #     while a is not None:
    #         print(a.data,end=" ")
    #         a=a.next

    def traverse(self):
        a=self
        print("Traversing the list...")
        while a is not None:
            print(a.data,end=" ")
            a=a.next
        print()

    def __len__(self):
        current = self
        l = 0
        while current is not None:
            l += 1
            current = current.next
        return l

    def insert(self, value):
        n = ListNode(value)
        n.next=self.next
        self.next=n

    def delete(self):
        '''
        removes the node from the linked list it is part of
        '''
        assert self is not None

        if self.next is None:
            self = None
        else:
            self.data = self.next.data
            self.next = self.next.next
            
        return self
    
    # def delete(self):
    #     item=None
    #     if self.next is not None:
    #         tmp=self.next
    #         item=tmp.data
    #         self.next=tmp.next
    #     return item

    def __repr__(self):
        return repr(self.data)