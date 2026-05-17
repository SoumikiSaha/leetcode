class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        from bisect import bisect_right

        # Stores last day each lake became full
        full_lakes = {}

        # Stores indices of dry days (days with 0)
        dry_days = []

        # Result array
        ans = [-1] * len(rains)

        for i in range(len(rains)):

            # Rainy day
            if rains[i] > 0:
                lake = rains[i]

                # If lake already full -> must dry it before today
                if lake in full_lakes:

                    # Find a dry day after previous rain day
                    prev_day = full_lakes[lake]

                    idx = bisect_right(dry_days, prev_day)

                    # No dry day available -> flood unavoidable
                    if idx == len(dry_days):
                        return []

                    # Use this dry day to dry current lake
                    dry_day = dry_days[idx]

                    ans[dry_day] = lake

                    # Remove used dry day
                    dry_days.pop(idx)

                # Mark lake as full today
                full_lakes[lake] = i

            # Sunny day
            else:
                dry_days.append(i)

                # Temporary value
                ans[i] = 1

        return ans