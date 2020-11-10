
# Куча

class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):
        while i != 0 and self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]

    def extract_min(self):
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        if not self.size:
            return None
        self.size -= 1
        self.sift_down(0)
        return tmp

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]


# Сортировка через кучу

def heapefy(arr):
    """Transform array to heap"""
    heap = Heap()
    for item in arr:
        heap.insert(item)
    return heap


def get_sorted_arr(heap):
    """Sorting"""
    arr = []
    while heap.size:
        arr.append(heap.extract_min())
    return arr

