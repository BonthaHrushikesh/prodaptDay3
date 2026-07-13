from collections import Counter
data= ["apple", "banana", "orange", "apple", "banana", "apple"]
counter = Counter(data)
print(counter)

from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'grade'])
student1 = Student(name='Alice', age=20, grade='A')
print(student1)


from collections import deque
queue = deque([1, 2, 3])
deque.append(4)
deque.appendleft(0)
print(queue)