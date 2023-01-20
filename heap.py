from queue import Queue


class PriorityQueue(Queue):
    def _init(self, maxsize):
        self.queue = []
    
    def _qsize(self):
        return len(self.queue)
    
    def _put(self, item):
        heappush(self.queue, item)
    
    def _get(self):
        return heappop(self.queue)


def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)


def heappop(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]

    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
