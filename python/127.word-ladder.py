class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        
        Idea: use bfs to calculate minimum path from beginWord to endWord
        
        N - number of word (size of dictionary)
        l - max length of words
        Time: O(N**2 * l)
        Space: O(N**2 * l)
        
        Algorithm:
        0) check if endWord is in wordList, otherwise return 0
        1) build adjacent list from wordList
        2) init queue, init visited set
        3) bfs while queue is not empty:
            pop word from queue
            check if word == endWord, then return distance + 1
            add to queue all unvisited vertices adjacent to word
        
        """
        
        if not endWord in wordList:
            return 0

        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '.' + word[i+1:]
                adj[pattern].append(word)
        
        queue = deque([(beginWord, 0)])
        visited = set(beginWord)
        
        while queue:
            word, dist = queue.pop()
            if word == endWord:
                return dist + 1
            
            for i in range(len(word)):
                pattern = word[:i] + '.' + word[i+1:]
                for adj_word in adj[pattern]:
                    if not adj_word in visited:
                        queue.appendleft((adj_word, dist + 1))
                        visited.add(adj_word)
        
        return 0