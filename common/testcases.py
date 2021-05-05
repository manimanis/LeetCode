def make_tests(testcases, class_to_test, func, prepare_data=None):
    sol = class_to_test()
    fun = getattr(sol, func)
    tc, ftn = 0, 0
    for inp, out in testcases:
        tc += 1
        if prepare_data is not None:
            inp = prepare_data(*inp)
        print(inp)
        res = fun(*inp)
        if res != out:
            print(f"Excpected: {out} - Result: {res}")
            print()
        else:
            print("OK")
            ftn += 1
    print(f"{ftn}/{tc} Passed!")
