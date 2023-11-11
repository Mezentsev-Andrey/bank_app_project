import functools
import datetime


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{datetime.datetime.now()} {func.__name__} ok"
            except Exception as e:
                result = None
                log_message = f"{datetime.datetime.now()} {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, 'a') as file:
                    file.write(log_message + '\n')
            else:
                print(log_message)

            return result

        return wrapper

    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

result = my_function( 3 , 3)
print(result)
#После выполнения этого кода, в файле mylog.txt должна появиться запись в формате, описанном в вопросе.
