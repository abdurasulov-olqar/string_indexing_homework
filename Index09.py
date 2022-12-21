import string

def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    ans = -1

    if s in string.digits:
        ans = int(s)
    return ans

