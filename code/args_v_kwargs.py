# from https://www.youtube.com/watch?v=GdSJAZDsCZA


def my_func():
    print("hello world")

my_func()


def my_func():
    print("hello world")

my_func("abc")



def my_func(*args):
    print("hello world", args)

my_func("abc", "abc", 123, "abc",)


def my_func(key=None, *args):
    print("hello world", args)

my_func("abc", "abc", 123, "abc", key=123)



def my_func(*args, **kwargs):
    print("hello world", args, kwargs)

my_func("abc", "abc", 123, "abc", key=123, abc=123)


def my_func(abc=None, *args, **kwargs):
    print("hello world", args, kwargs)

my_func("abc", abc=123)


def my_func(abc=None, *args, **kwargs):
    print("hello world", args, kwargs)

my_func(abc=123)


def my_func(abc=None, *args, **kwargs):
    print("hello world", args, kwargs)

my_func(abc=123, "abc")


def my_func(arg_1, *args, **kwargs):
    print("hello world", args, kwargs)

my_func(abc=123, "abc")


def my_func(*args, **kwargs):
    print("hello world", args, kwargs)

my_func("abc", abc=123)


def my_random_django_view(request, **kwargs):
    print(kwargs)
    # Product.objects.get(id=kwargs.get('id'))

# path('my-product/:id')
my_random_django_view("request", id='some_id')
