class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None

    def Push(self,new_data):
        newNode = Node(new_data)  #make new node 
        newNode.next = self.head  # -->[ , node1 , node2] make shifting to left to right to make first place empty
        self.head = newNode  # new node as first node
    
    def Append(self,new_data):
        newNode = Node(new_data)  

        if self.head is None:
            self.head = newNode
            return 

        temp = self.head
        while(temp.next):
            temp = temp.next  

        temp.next = newNode

    def insertAfter(self , prevNode , new_data):
        newNode = Node(new_data) 

        if prevNode is not None:
            newNode.next = prevNode.next
            prevNode.next = newNode
        else : 
            print("previous node should be not none")

    def Pop(self):
        print(self.head)
        self.head = self.head.next

    def Get(self,Index):
        temp = self.head
        while(Index != 0):
            temp = temp.next
            Index-=1
        return temp
    
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':

    llist = LinkList()
    llist.Push(5)
    llist.Push(6)
    llist.Push(8)
    llist.printList()
    llist.insertAfter(llist.head, 9)
    llist.printList()
    llist.Pop()
    llist.printList()
    print(llist.Get(0).data)
