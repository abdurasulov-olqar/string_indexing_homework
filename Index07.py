def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """ 
    ans = False

    if n <= (len(s)-1):
        ans = s[n] 
    return ans
