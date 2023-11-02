import time

class DevilError(Exception):
    pass

def message_decorator(func):
    def wreaper(*args, **kwargs):
        print('начало выполнение функции')
        psina = func(*args, **kwargs)
        print('функция закончила свое выполнение')
        return psina 
    return wreaper

def time_it(func):
    def wreaper(*args, **kwargs):
        start = time.time()
        a = func(*args, **kwargs)
        time.sleep(1)
        finish = time.time()
        print (f'функция выполнилась: {finish-start}')
        return a 
    return wreaper

def catch_exceptions(func):
    def wreaper(*args, **kwargs):
        try:
            s = func(*args, **kwargs)
        except DevilError as e:
            print(f'Ошибка: {e}')
            return None   
        return s
    return wreaper

@time_it
@message_decorator 
@catch_exceptions
def gnida(x):
    result = x+10
    if result == 666:
        raise DevilError('')
    return result

print(gnida(656))
