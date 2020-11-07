import time
import functools

def clocks(func):
    @functools.wraps(func)
    def clocked(*args, **kewargs):
        t0 = time.time()
        result = func(*args, **kewargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(','.join(repr(arg) for arg in args))
        if kewargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(','.join(pairs))
        arg_str = ','.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked
