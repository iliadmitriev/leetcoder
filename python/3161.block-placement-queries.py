import operator as op


class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        if not queries:
            return []

        get_type = op.itemgetter(0)
        get_coord = op.itemgetter(1)
        get_size = op.itemgetter(2)
          
        max_x = max(map(get_coord, queries))

        size = max_x + 2
        bit = [0] * (size + 1) # 1-indexed BIT array

        blocks_mask = 1 # bit 0 is set (left boundary)
        type1_pos = []

        for q in queries:
            if get_type(q) == 1:
                x = get_coord(q)
                blocks_mask |= 1 << x
                type1_pos.append(x)

        # right boundary obstacle
        blocks_mask |= 1 << (max_x + 1)

        # init with gaps
        prev_obs = 0
        for x in sorted(type1_pos):
            gap = x - prev_obs
            idx = x + 1

            while idx <= size:
                bit[idx] = max(bit[idx], gap)
                idx += idx & -idx
            
            prev_obs = x

        gap = (max_x + 1) - prev_obs
        idx = max_x + 2

        while idx <= size:
            bit[idx] = max(bit[idx], gap)
            idx += idx & -idx

        num_type2 = sum(1 for q in queries if get_type(q) == 2)
        results = [False] * num_type2
        res_idx = num_type2 - 1

        for q in reversed(queries):
            if get_type(q) == 1:
                x = get_coord(q)
                m_next = blocks_mask & ~((1 << (x + 1)) - 1)
                if m_next:
                    after = (m_next & -m_next).bit_length() - 1
                    m_prev = blocks_mask & ((1 << x) - 1)

                    if m_prev:
                        before = m_prev.bit_length() - 1

                        idx = after + 1
                        new_gap = after - before
                        while idx <= size:
                            bit[idx] = max(bit[idx], new_gap)
                            idx += idx & -idx

                blocks_mask &= ~(1 << x)
            else:
                x, sz = get_coord(q), get_size(q)
                
                # Rightmost obstacle <= x
                m_prev = blocks_mask & ((1 << (x + 1)) - 1)
                last_obs = m_prev.bit_length() - 1 if m_prev else 0

                idx = x + 1
                max_gap = 0

                while idx > 0:
                    max_gap = max(max_gap, bit[idx])
                    idx -= idx & -idx

                trailing = x - last_obs
                max_gap = max(max_gap, trailing)

                results[res_idx] = max_gap >= sz
                res_idx -= 1


        return results
              