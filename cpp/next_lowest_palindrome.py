
"""
19 <- number of test cases
7
77
101
1001
1221
144441
3444444443
57855875
10000001
11
1
111
101
1001
11011
1110111 # 1109011
1190911 # 1189811
20002
10011001
"""

a = "20002"
def nl_palindrome(N: str) -> None:
    a_len = len(N)
    if a_len == 1:
        res = 0

    else:
        idx = int(round((a_len / 2) + 0.5, 0))
        b1 = N[:idx]
        b2 = str(int(b1) - 1)

        # if len(b2) < len(b1):
        #     b2 += "9"

        if a_len % 2 != 0:
            subidx = idx - 1
            res = b2 + b2[:subidx][::-1]
        else:
            res = b2 + b2[::-1]

    print(res)

nl_palindrome(a)
nl_palindrome("11")