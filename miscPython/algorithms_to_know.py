def binary_search(array,value):
    if not array:
        raise ValueError("value not in array")
    index = len(array)//2
    middle_value = array[index]
    if middle_value < value:
        return index + 1 + binary_search(array[index+1:],value)
    elif middle_value > value:
        return binary_search(array[:index],value)
    return index

def fixed_sliding(array, k):
    current = sum(array[:k])
    best = current
    for i in range(k,len(array)):
        current += array[i] - array[i-k]
        best = max(best, current)
    return best

def variable_sliding(array, max_sum):
    start, best, current = 0, 0, 0
    for end in range(len(array)):
        current += array[end] #move end index to the right each iteration
        while current >= max_sum:
            current -= array[start] #while sum is too large, move start index to the right
            start += 1
        best = max(best, end - start + 1)
    return best

from collections import deque

def bfs(graph,visited):
    visited = set()
    order = []
    queue = deque([start])
    
    while len(queue) > 0:
        v = queue.leftpop()
        if v not in visited:
            visited.add(v)
            order.append(v)
            for w in graph.get(v,[]):
                if w not in visited:
                    queue.append(w)
    return order

def dfs(graph,v,visited,order): #pre-order dfs
    visited.add(v)
    order.append(v)
    for w in graph.get(v,[]):
        if w not in visited:
            dfs(graph,w,visited,order)

def depth_first_search(graph,start):
    visited = set()
    order = []
    dfs(graph,start,visited,order)
    return order


