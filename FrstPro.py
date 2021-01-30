class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = node(4)
    second = node(5)
    third = node(8)
    llist.head.next = second
    second.next = third
    llist.printList()
