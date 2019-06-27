def e_approx(n):
    e = 1.0
    start = 1.0
    for i in range(1,n+1):
        start *= i
        e += (1/start)
    return e


# def main():
#     for n in range(15):
#         curr_approx = e_approx(n)
#         approx_str = "{:15f}".format(curr_approx)
#         print('n =',n,"Approxiamation:",approx_str)
#
# main()
