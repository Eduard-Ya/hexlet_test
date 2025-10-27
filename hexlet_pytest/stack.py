stack = []  # В Python стек реализован через список
not stack  # Список пуст
# True
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
not stack  # Список не пустой
# False
stack
# [1, 2, 3]
stack.pop()  # В стеке [1, 2]
# 3
stack.pop()  # В стеке [1]
# 2
stack.pop()  # В стеке пусто
# 1
not stack
# True