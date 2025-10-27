import pytest


def test_pop_with_empty_stack():
    stack = []
    # проверить что вызывается конкретное исключение можно с помощью конструкции with pytest.raises()
    # если внутри блока вызовется исключение, то тест будет пройден
    with pytest.raises(IndexError):
        stack.pop()