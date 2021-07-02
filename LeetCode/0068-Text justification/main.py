"""  
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters 
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line 
do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots 
on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.",
"Art","is","everything","else","we","do"], maxWidth = 20

Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur_line, num_of_char = [], [], 0

        for word in words:
            # num_of_char: number of chars corresponding to the words in cur_line
            # len(cur_line): the number of space if new word is added
            # len(word): current word length
            # so the line below is the minimum length if current word is adde to the cur_line
            if num_of_char + len(cur_line) + len(word) > maxWidth:
                # we use max. 1 because atleast one word would be there and to avoid modulo by 0
                size = max(len(cur_line) - 1, 1)

                # maxWidth - num_of_char = num_of_space
                for i in range(maxWidth - num_of_char):
                    # insert the space between words in round robin manner
                    cur_line[i % size] += ' '

                res.append(''.join(cur_line))
                cur_line, num_of_char = [], 0

            cur_line.append(word)
            num_of_char += len(word)

        # add last line to the res and pack space to the right
        res.append(' '.join(cur_line).ljust(maxWidth))
        return res
