
def leftChild(n):
    return 2 * n + 1

def rightChild(n):
    return 2 * n + 2

def minHeapify(heap):
    n = len(heap)
    for i in range(n // 2):
        isHeap = False
        indexToSwap = i

        while isHeap == False and leftChild(i) < n:
            if heap[leftChild(i)]["element"] < heap[indexToSwap]["element"]:
                indexToSwap = leftChild(i)
            if rightChild(i) < n:
                if heap[rightChild(i)]["element"] < heap[indexToSwap]["element"]:
                    indexToSwap = rightChild(i)
            if indexToSwap == i:
                isHeap = True
            else:
                # Swap
                heap[i], heap[indexToSwap] = heap[indexToSwap], heap[i]
                i = leftChild(i)


def findMinRange(lists, listCount):
    heap = []
    minRange = 100
    max = 0
    min = 100
    # Initialization
    for i in range(listCount):
        temp = {}
        temp["index"] = 0
        temp["listNumber"] = i
        temp["element"] = lists[i][0]
        heap.append(temp)
        if temp["element"] > max:
            max = temp["element"]
    
    # print(heap)
    minHeapify(heap)
    min = heap[0]["element"]
    minRange = max - min 
    # print(heap)

    while True:
        currentList = heap[0]["listNumber"]
        currentIndex = heap[0]["index"] + 1
        if currentIndex == len(lists[currentList]):
            return min, max, minRange
        element = lists[currentList][currentIndex]
        heap[0]["element"] = element
        heap[0]["index"] += 1
        if element > max:
            max = element
        minHeapify(heap)
        min = heap[0]["element"]
        currentRange = max - min
        if currentRange < minRange:
            minRange = currentRange

l1 = [4, 10, 15, 24, 26]
l2 = [0, 9, 12, 20]
l3 = [5, 18, 22, 30]
lists = [l1, l2, l3]
print(findMinRange(lists, len(lists)))



         

