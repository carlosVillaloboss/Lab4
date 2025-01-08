class NodoDoble:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addLast(self, data):
        nuevo_nodo = NodoDoble(data)
        if self.isEmpty():
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            nuevo_nodo.prev = self.tail
            self.tail = nuevo_nodo
        self.size += 1
    
    def addFirst(self, data):
        new_node = NodoDoble(data)
        if self.head is None:  # La lista está vacía
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Si es el primer nodo
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # Si es el último nodo
                self.size -= 1
                return True
            current = current.next
        return False  # Si no encuentra el nodo

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next
        print("None")
