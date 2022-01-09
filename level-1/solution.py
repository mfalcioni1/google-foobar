import string

letters = list(string.ascii_letters)
lower_letters = [i for i in letters if i.islower()]

def solution(x):
    """
    Takes a string input and decodes it.
    The crypto key is simply an inverted alphabet.
    parameters
        input (str): a string to be decoded
    returns
        res (str): the decoded string
    """
    res = ""
    for i in x:
        if i in lower_letters:
            # then transpose
            idx = lower_letters.index(i)
            n_idx = abs(idx - 25) # n-1 letters
            d_x = lower_letters[n_idx]
            res = res + d_x
        else:
            res = res + i
    
    return res

# examples
# solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
# solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")