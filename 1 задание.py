class Stack:
    def __init__(self, capacity=10):
        self.top_index = -1  # индекс вершины стека
        self.stack = [None] * capacity
        self.capacity = capacity

    def push(self, value):
        if self.top_index >= self.capacity - 1:
            print("Ошибка: стек переполнен.")
            return
        self.top_index += 1
        self.stack[self.top_index] = value

    def pop(self):
        if self.is_empty():
            print("Ошибка: стек пустой.")
            return None
        value = self.stack[self.top_index]
        self.stack[self.top_index] = None  # очистка значения (по желанию)
        self.top_index -= 1
        return value

    def top(self):
        if self.is_empty():
            print("Ошибка: стек пустой.")
            return None
        return self.stack[self.top_index]

    def is_empty(self):
        return self.top_index == -1


s = Stack()

s.push(10)
s.push(20)
print("Вершина:", s.top())  # 20
print("Удалено:", s.pop())  # 20
print("Вершина после pop:", s.top())  # 10
print("Стек пуст?", s.is_empty())  # False
s.pop()
s.pop()
