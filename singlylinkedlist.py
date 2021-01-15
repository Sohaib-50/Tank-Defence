class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.__length = 0

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
        return self.__length
        # a = self
        # i=0
        # while a is not None:
        #     i+=1
        #     a = a.next
        # return i

    def insert(self, value):
        n = ListNode(value)
        n.next=self.next
        self.next=n
        self.__length += 1


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

        self.__length -= 1
    # def delete(self):
    #     item=None
    #     if self.next is not None:
    #         tmp=self.next
    #         item=tmp.data
    #         self.next=tmp.next
    #     return item