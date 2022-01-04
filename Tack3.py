
class TypeDecorators:

    def to_bool(self):
        def decorator(func):
            if func.isalpha() and func.capitalize() == 'True' and type(func) == str:
                return True
            raise Exception('Err value')
        return decorator

    def to_str(self):
        def decorator(func):
            return str(func)
        return decorator

    def to_float(self):
        def decorator(func):
            if type(func) == int:
                return float(func)
            raise TypeError('Err type')
        return decorator

    def to_int(self):
        def decorator(func):
            if func.isdigit() and type(func) == str:
                return int(func)
            raise Exception('Err value')
        return decorator


@TypeDecorators.to_int
def do_nothing(string: str):
    return string
@TypeDecorators.to_bool
def do_something(string: str):
    return string
@TypeDecorators.to_float
def floating_nothing(value: int):
    return value
@TypeDecorators.to_str
def something(value):
    return value

