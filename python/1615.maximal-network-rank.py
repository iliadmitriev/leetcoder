class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for u, v in roads:
            degree[v] += 1
            degree[u] += 1
        
        sorted_degree = sorted(degree, reverse=True)

        first = sorted_degree[0]
        second = sorted_degree[1] if len(sorted_degree) > 1 else 0

        first_count = sorted_degree.count(first)
        second_count = sorted_degree.count(second)
        
        # if there is multiple cities have max degree
        if first_count > 1:
            # number of directly connected cities with max degree
            first_connected = sum(1 for u, v in roads if degree[u] == first and degree[v] == first)
            # number of all possible theoretical connections (fully connected)
            possible_connected = first_count * (first_count - 1) // 2
            # if all cities with max degree is connected then
            # there is no cities that are not connected and we have to reduce rank by 1
            # for the connection
            rank = first + first
            return rank - 1 if first_connected == possible_connected else rank

        # apply the same idea
        # count number of connections between cities of first degree and second degree
        # if it's equal to max possible number of connections
        # then all cities are connected
        # then there is no pair of not connected cities
        # and we have to reduce rank by one for the connection
        first_to_second = sum(1 for u, v in roads if (degree[u], degree[v]) in [(first, second), (second, first)])
        rank = first + second
        return rank - 1 if second_count == first_to_second else rank

        
        