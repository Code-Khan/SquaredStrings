# This kata is the first of a sequence of four about "Squared Strings".

# You are given a string of n lines, each substring being n characters long: For example:

# s = "abcd\nefgh\nijkl\nmnop"

# We will study some transformations of this square of strings.

# Vertical mirror: vert_mirror (or vertMirror or vert-mirror)
# vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"
# Horizontal mirror: hor_mirror (or horMirror or hor-mirror)
# hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"
# or printed:

# vertical mirror   |horizontal mirror   
# abcd --> dcba     |abcd --> mnop 
# efgh     hgfe     |efgh     ijkl 
# ijkl     lkji     |ijkl     efgh 
# mnop     ponm     |mnop     abcd 
# Task:

# Write these two functions
# and

# high-order function oper(fct, s) where

# fct is the function of one variable f to apply to the string s (fct will be one of vertMirror, horMirror)

# Examples:

# s = "abcd\nefgh\nijkl\nmnop"
# oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
# oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd"
# Note:

# The form of the parameter fct in oper changes according to the language. You can see each form according to the language in "Sample Tests".

# Bash Note:

# The input strings are separated by , instead of \n. The output strings should be separated by \r instead of \n. See "Sample Tests".

# Solution in Python # 

def vert_mirror(strng):
    split_strng = strng.split('\n')
    len_ = len(split_strng[0])
    final_string = []
    
    for i in split_strng:
        final_string.append(i[::-1])
    
    final = ''.join(final_string)
    final_ = '\n'.join(final[i:i+len_] for i in range(0, len(final), len_))
    return final_
    
def hor_mirror(strng):
    split_strng = strng.split('\n')
    len_ = len(split_strng[0])
    final_strng = split_strng[::-1]
    
    final = ''.join(final_strng)
    final_ = '\n'.join(final[i:i+len_] for i in range(0, len(final), len_))
    return final_
    
def oper(fct, s):
    return fct(s)

