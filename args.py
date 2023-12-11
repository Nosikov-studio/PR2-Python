def func1(*args, **kwargs):
    print(f"args:{args}")
    print(f"kwargs:{kwargs}")


def mix(first, *args, **kwargs):
    print(first)
    print(args)
    print(kwargs)


func1(1, 2, 3, name="Evgeny")
mix("apple", "cherry", x=3)
