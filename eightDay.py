def now():
    print('2015-1-1')


f = now
f()
print(now.__name__)
print(f.__name__)


def log(func):
    def wapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wapper


@log
def now():
    print('2232-13-1')


now()
print(now.__name__)

'''装饰器学习'''


def foo():
    print('foo')


foo
foo()

'''神策数据的笔试题'''
a = [1, 0, 1, 2, 4, 0, 2, 5, 6, 34, 5, 2, 53, 0]
l = list(filter(lambda x: x != 0, a)) + list(filter(lambda x: x == 0, a))

print(l)
