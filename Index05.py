import string

def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    ans = 0

    ans += s[0] in string.digits
    ans += s[1] in string.digits
    ans += s[2] in string.digits
    ans += s[3] in string.digits
    ans += s[4] in string.digits
    return ans


