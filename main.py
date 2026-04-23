def alien_dictionary(words):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = {c: 0 for word in words for c in word}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                indegree[w2[j]] += 1
                break
        else:
            if len(w1) > len(w2): return ""
    queue = deque([c for c in indegree if indegree[c] == 0])
    result = []
    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return "".join(result) if len(result) == len(indegree) else ""

print(alien_dictionary(["wrt","wrf","er","ett","rftt"]))
