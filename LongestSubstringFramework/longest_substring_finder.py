class LongestSubstringFinder:

    def __init__(self, input_string):
        self.input_string = input_string

    def all_unique(self, substring):
        return len(set(substring)) == len(substring)

    def find_longest_substring(self):
        n = len(self.input_string)
        max_len = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = self.input_string[i:j]
                if self.all_unique(substring):
                    max_len = max(max_len, len(substring))
        return max_len