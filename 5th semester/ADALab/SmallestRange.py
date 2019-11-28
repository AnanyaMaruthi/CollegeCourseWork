import sys

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
    minRange = sys.maxsize
    minGlobal = sys.maxsize 
    maxGlobal = -1
    # Initialization
    for i in range(listCount):
        temp = {}
        temp["index"] = 0
        temp["listNumber"] = i
        temp["element"] = lists[i][0]
        heap.append(temp)
        if temp["element"] > maxGlobal:
            maxGlobal = temp["element"]
    
    # print(heap)
    minHeapify(heap)
    minGlobal = heap[0]["element"]
    minRange = maxGlobal - minGlobal 
    # print(heap)

    min = minGlobal
    max = maxGlobal
    while True:
        currentList = heap[0]["listNumber"]
        currentIndex = heap[0]["index"] + 1
        if currentIndex == len(lists[currentList]):
            return minGlobal, maxGlobal, minRange

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
            maxGlobal = max
            minGlobal = min

l1 = [4, 10, 15, 24, 26]
l2 = [0, 9, 12, 20]
l3 = [5, 18, 22, 30]
l1 = [4, 7, 9, 12, 15]
l2 = [0, 8, 10, 14, 20]
l3 = [6, 12, 16, 30, 50]
lists = [l1, l2, l3]
print(findMinRange(lists, len(lists)))



         

