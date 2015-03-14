class ListNode():
    def __init__(self, element=-1):
        self.element = element
        self.next = None
        self.front = None


class List():
    def __init__(self, node):
        self.head = node

    # O(1)
    def empty(self):
        return self.head.next is None

    # O(n)
    def insert_before(self, element, node):
        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
            if temp_node is node:
                node.element = element
                # define some temp
                temp_front = temp_node.front

                temp_front.next = node
                node.front = temp_front

                node.next = temp_node
                temp_node.front = node
                return True
        return False

    # O(n)
    def insert_after(self, element, node):
        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
            if temp_node is node:
                node.element = element
                temp_next = temp_node.next

                temp_node.next = node
                node.front = temp_node

                node.next = temp_next
                temp_next.front = node
                return True
        return False

    # O(n)
    def count(self):
        temp_node = self.head
        _count = 0
        while temp_node is not None:
            _count += 1
        return _count

    # O(1)
    def first_object(self):
        if self.empty():
            return None
        return self.head.next

    # O(n)
    def last_object(self):
        if self.empty():
            return None
        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next

        return temp_node

    # O(n)
    def find(self, element):
        temp_node = self.head
        while temp_node.next is not None:
            if temp_node.element == element:
                return True

        return False


def test_empty():
    head = ListNode(-1)
    list = List(head)
    assert list.empty()
    node = ListNode(0)
    head.next = node
    assert list.empty()


def test_insert_before():
    head = ListNode(-1)
    list = List(head)
    node = ListNode(0)
    node1 = ListNode(0)
    node2 = ListNode(0)

    head.next = node
    node.front = head
    node.next = node1
    node1.front = node
    node1.next = node2
    node2.front = node1

    assert list.insert_before(1, node2)
    assert list.insert_before(1, ListNode())


def test_insert_after():
    head = ListNode(-1)
    list = List(head)
    node = ListNode(0)
    node1 = ListNode(0)
    node2 = ListNode(0)

    head.next = node
    node.front = head
    node.next = node1
    node1.front = node
    node1.next = node2
    node2.front = node1

    assert list.insert_after(1, node1)
    assert list.insert_after(1, ListNode())


def test_count():
    head = ListNode(-1)
    list = List(head)
    node = ListNode(0)
    node1 = ListNode(0)
    node2 = ListNode(0)

    head.next = node
    node.front = head
    node.next = node1
    node1.front = node
    node1.next = node2
    node2.front = node1

    assert list.count()


def test_first_object():
    head = ListNode(-1)
    list = List(head)
    assert list.first_object()
    node = ListNode(0)
    node1 = ListNode(0)
    node2 = ListNode(0)

    head.next = node
    node.front = head
    node.next = node1
    node1.front = node
    node1.next = node2
    node2.front = node1

    assert list.first_object()


def test_last_object():
    head = ListNode(-1)
    list = List(head)
    assert list.last_object()
    node = ListNode(0)
    node1 = ListNode(0)
    node2 = ListNode(0)

    head.next = node
    node.front = head
    node.next = node1
    node1.front = node
    node1.next = node2
    node2.front = node1

    assert list.last_object()


def test_find():
    head = ListNode(-1)
    list = List(head)
    assert list.find(0)
    node = ListNode(0)
    node1 = ListNode(0)
    node2 = ListNode(0)

    head.next = node
    node.front = head
    node.next = node1
    node1.front = node
    node1.next = node2
    node2.front = node1
    assert list.find(1)
    assert list.find(7)


test_empty()
test_insert_before()
test_insert_after()
test_count()
test_first_object()
test_last_object()
test_find()