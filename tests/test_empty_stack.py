def test_emptiness():
    stack = []
    assert not stack
    stack.append("one")
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack