class QueueError(Exception):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
       self.__list = []
       self.__count = 0

    def put(self, elem):
        self.__list.insert(0, elem)

    def get(self):
        try :
            return(self.__list.pop())
        except QueueError:
            pass


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
