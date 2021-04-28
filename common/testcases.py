def make_tests(testcases, class_to_test, func, prepare_data=None):
    sol = class_to_test()
    fun = getattr(sol, func)
    for inp, out in testcases:
        print(inp)
        if prepare_data is not None:
            inp = prepare_data(*inp)
        res = fun(*inp)
        print(f"{res} == {out} = {res == out}")
        print()
