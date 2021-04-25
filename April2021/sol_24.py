"""Critical Connections in a Network.
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3719/
"""
from typing import List


class Solution:
    @staticmethod
    def browseAll(n, nodes, node):
        visited = [False for _ in range(n)]
        queue = []
        numComponents = 0
        nodes[node[0]].remove(node[1])
        nodes[node[1]].remove(node[0])
        for i in range(n):
            if not visited[i]:
                queue.append(i)
                numComponents += 1
            while len(queue) > 0:
                server = queue.pop(0)
                if not visited[server]:
                    for other in nodes[server]:
                        if not visited[other]:
                            queue.append(other)
                visited[server] = True
        nodes[node[0]].append(node[1])
        nodes[node[1]].append(node[0])
        return numComponents

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        nodes = {i: [] for i in range(n)}
        crit = []
        for con in connections:
            f, t = min(con), max(con)
            nodes[f] += [t]
            nodes[t] += [f]
        for con in connections:
            if Solution.browseAll(n, nodes, con) > 1:
                crit.append(con)
        return crit

    def criticalConnections(self, n, connections):
        """La solution fonctionnelle"""
        used, tin, fup = [0]*n, [-1]*n, [-1]*n
        self.timer, ans = 0, []
        graph = defaultdict(list)
        
        def dfs(node, par = -1):
            used[node] = 1
            tin[node] = fup[node] = self.timer + 1
            self.timer += 1
            for child in graph[node]:
                if child == par: continue
                if used[child] == 1:
                    fup[node] = min(fup[node], tin[child])
                else:
                    dfs(child, node)
                    fup[node] = min(fup[node], fup[child])
                    if fup[child] > tin[node]: ans.append([node, child])
        
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
            
        for i in range(n):
            if not used[i]: dfs(i)
                
        return ans


test_cases = [
    (4, [[0,1],[1,2],[2,0],[1,3]]), # [[1, 3]]
    (6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]) # [[1, 3]]
]
sol = Solution()
for case in test_cases:
    print(case)
    print(sol.criticalConnections(*case))
    print()
    print()