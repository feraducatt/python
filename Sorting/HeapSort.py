# order a binary heap tree by putting it into
# an array starting at 1
# i//2 is the location of the parent
# i*2 is the location of the child
# MaxHeap operations: Push(insert) Peek(get max) Pop (remove max)
class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else: max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[parent] < self.heap[index]:
            self.__swap(parent, index)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest  = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

def heap_sort(arr):
    m = MaxHeap(arr)
    for i in range(0, len(arr)):
        arr[-i-1] = m.pop()


if __name__ == "__main__":
    arr = [12,3,4,34,45,56,6,5,34,342,23,4,3,1,9,0,989,5]
    heap_sort(arr)
    print(arr)



