from Chapter8_Queues.linkedqueue import LinkedQueue
from Chapter8_Queues.arrayqueue import ArrayQueue


def test(queueType):
    # Test any implementation with the same code.
    s = queueType()
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    print("Add 1-10")
    for i in range(10):
        s.add(i + 1)
    print("Items (top to bottom):", s)
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    theClone = queueType(s)
    print("Items in clone (top to bottom):", theClone)
    theClone.clear()
    print("Length of clone after clear:", len(theClone))
    print("Push 11")
    s.add(11)
    print("Popping items (top to bottom):", end="")
    while not s.isEmpty():
        print(s.pop(), end=" ")
    print("\nLength:", len(s))
    print("Empty:", s.isEmpty())


test(ArrayQueue)


# def test2(queueType):
#     q = queueType()
#     q.add(1)
#     q.add(2)
#     q.add(3)
#     q.pop()
#     q.pop()
#     q.add(4)
#     print(q)
#     print(q._front)
#     print(q._rear)


