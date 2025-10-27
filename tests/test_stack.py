def test_stack():
    stack = []
    # Добавляем два элемента в стек и затем извлекаем их
    # Почему два? Так надежнее, чем один, а три — уже избыточно
    stack.append("one")
    stack.append("two")

    assert stack.pop() == "two"
    assert stack.pop() == "one"