def func():
    a=5
    def fun():
        nonlocal a
        a=10
        print("inner function",a)
    fun()
    print("outer function",a)
func()
