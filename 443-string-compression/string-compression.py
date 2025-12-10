class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0            # where to write in chars[]
        read = 0             # scan the array

        while read < len(chars):
            char = chars[read]
            count = 0

            # count consecutive repeating chars
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # write the character
            chars[write] = char
            write += 1

            # write the count if > 1
            if count > 1:
                for c in str(count):   # handles 2-digit, 3-digit counts
                    chars[write] = c
                    write += 1

        return write
