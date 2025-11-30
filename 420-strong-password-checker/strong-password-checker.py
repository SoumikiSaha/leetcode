class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        # Count missing types
        missing_lower = 1
        missing_upper = 1
        missing_digit = 1
        for ch in password:
            if ch.islower(): missing_lower = 0
            if ch.isupper(): missing_upper = 0
            if ch.isdigit(): missing_digit = 0
        missing_types = missing_lower + missing_upper + missing_digit

        # Find repeating sequences of length >= 3
        repeats = []
        i = 2
        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                while i < n and password[i] == password[i-1]:
                    length += 1
                    i += 1
                repeats.append(length)
            else:
                i += 1

        # Case 1: too short
        if n < 6:
            return max(missing_types, 6 - n)

        # Case 2: length ok
        if n <= 20:
            replace = sum(length // 3 for length in repeats)
            return max(missing_types, replace)

        # Case 3: too long -> must delete
        delete_needed = n - 20

        # Prioritise deletions to reduce replacements efficiently:
        # First consider runs where length % 3 == 0, then ==1, then ==2
        counts = repeats[:]  # mutable copy
        for k in range(3):
            for idx in range(len(counts)):
                if delete_needed > 0 and counts[idx] >= 3 and counts[idx] % 3 == k:
                    # remove up to (k+1) chars here to reduce one replacement
                    need = min(delete_needed, k + 1)
                    counts[idx] -= need
                    delete_needed -= need

        # If deletes still remain, apply them anywhere (they will reduce replacements further)
        # (Remaining deletes will just shorten sequences; we can subtract them greedily)
        if delete_needed > 0:
            # Any further deletes just shrink groups; we can apply them to any counts >= 3
            for idx in range(len(counts)):
                if delete_needed == 0:
                    break
                if counts[idx] >= 3:
                    can_remove = min(delete_needed, counts[idx] - 2)
                    counts[idx] -= can_remove
                    delete_needed -= can_remove

        # After all deletions, compute remaining replacements
        replace = sum(c // 3 for c in counts)

        return (n - 20) + max(missing_types, replace)
