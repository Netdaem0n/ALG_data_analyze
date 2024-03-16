#Пример использования декоратора
def decorator(*args, **kwargs):
    """Simple decorator"""
    print("This is my decorator 1")
    print(f"Arguments: {args}")
    print(f"Kwargs: {kwargs}")

    def wrapper(func):
        def wrapper_inner(*args_inner, **kwargs_inner):
            print("Calling from new function")
            return func(*args_inner, **kwargs_inner)
        return wrapper_inner
    return wrapper


@decorator('1111111', **{'name': 'test', 'id': 123})
def hello(data):
    """Simple function that prints hello"""
    print(f"Hello World!!! {data}", hello.__name__, hello.__doc__, sep='\n')


hello("Ivan")
