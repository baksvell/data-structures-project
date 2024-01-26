from src.stack import Node, Stack


def test_node_initialization():
    n1 = Node(10, None)
    assert n1.data == 10
    assert n1.next_node is None

    n2 = Node(20, n1)
    assert n2.data == 20
    assert n2.next_node is n1


def test_stack_initialization():
    stack = Stack()
    assert stack.top is None


def test_stack_push():
    stack = Stack()
    stack.push(10)
    assert stack.top.data == 10
    assert stack.top.next_node is None

    stack.push(20)
    assert stack.top.data == 20
    assert stack.top.next_node.data == 10
