class Solution:
    def get_words(self, i: int, max_width: int, words: List[str]) -> List[str]:
        """Count words than fit into the line of max_width starting from the i-th word."""
        current_line = []
        curr_length = 0

        while i < len(words) and curr_length + len(words[i]) <= max_width:
            current_line.append(words[i])
            curr_length += len(words[i]) + 1
            i += 1
        
        return current_line
    
    def create_line(self, line: List[str], i: int, max_width: int, words: List[str]) -> str:
        """Builds a line of text from words."""
        base_length = reduce(lambda x, y: x + y + 1, map(len, line), -1)

        extra_spaces = max_width - base_length

        # if line consist of 1 word, or it's a last line
        if len(line) == 1 or i == len(words):
            # just join the line and add extra spaces at the end of line
            return ' '.join(line) + ' ' * extra_spaces

        word_count = len(line) - 1  # last word don't need space
        spaces_per_word = extra_spaces // word_count
        needs_extra_space = extra_spaces % word_count

        for j in range(needs_extra_space):
            line[j] += ' '

        for j in range(word_count):
            line[j] += ' ' * spaces_per_word

        return ' '.join(line)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []
        i = 0

        while i < len(words):
            curr_line = self.get_words(i, maxWidth, words)
            i += len(curr_line)
            res.append(self.create_line(curr_line, i, maxWidth, words))

        return res