def make_tests(testcases, class_to_test, func, prepare_inp=None, prepare_res=None):
    sol = class_to_test()
    fun = getattr(sol, func)
    tc, ftn = 0, 0
    for inp, out in testcases:
        tc += 1
        if prepare_inp is not None:
            inp = prepare_inp(*inp)
        print(inp)
        res = fun(*inp)
        if prepare_res is not None:
            res = prepare_res(res)
        if res != out:
            print(f"Excpected: {out} - Result: {res}")
            print()
        else:
            print("OK")
            ftn += 1
    print(f"{ftn}/{tc} Passed!")
