class Node:
    def __init__(self, id, prev=None, next=None):
        self.id = id
        self.prev = prev
        self.next = next
    
    def __eq__(self, comp):
        if self.id == comp.id and self.prev == comp.prev and self.next == comp.next:
            return True
        return False


class Table:
    def __init__(self, n, k):
        self.graph = {i: Node(i, i-1, i+1) for i in range(1, n-1)}
        self.graph[0] = Node(0, None, 1)
        self.graph[n-1] = Node(n-1, n-2, None)
        
        if k == 0:
            self.cursor = Node(0, None, 1)
        elif k == n-1:
            self.cursor = Node(n-1, n-2, None)
        else:
            self.cursor = Node(k, k-1, k+1)
        
        self.stack = []
        self.status = ["O"] * n
    
    def down(self, step):
        while step:
            self.cursor = self.cursor.next
            step -= 1
    
    def up(self, step):
        while step:
            self.cursor = self.cursor.prev
            step -= 1
    
    def cancel(self):
        self.stack.append(self.cursor)
        self.status[self.cursor.id] = 'X'
        
        _prev = self.cursor.prev
        if _prev is not None:
            _prev.next = _next
            self.graph[_prev.id] = _prev
        
        _next = self.cursor.next
        if _next is not None:
            _next.prev = _prev
            self.graph[_next.id] = _next
    
    def undo(self):
        node = self.stack.pop()
        current = self.graph[node.id]
        node.prev.next = node
        node.next.prev = node
        self.graph[node.prev.id] = node.prev
        self.graph[node.next.id] = node.next
        
        self.status[node.id] = 'O'
    
    def repr(self):
        return ''.join(self.status)


def solution(n, k, cmd):
    table = Table(n, k)
    
    for key in cmd:
        if len(key) > 1:
            ind, _walk = key.split()
            walk = int(_walk)
            if ind == "D":
                table.down(walk)
            elif ind == "U":
                table.up(walk)
            else:
                raise Exception()
        else:
            ind = key
            if ind == "C":
                table.cancel()
            elif ind == "Z":
                table.undo()
            else:
                raise Exception()

    return table.repr()
