from datetime import datetime

# original function
def greet(name):
    print('hello {}'.format(name))

# wrapper function
def timeWrapper(fn):
    # new_func accept any types of argument
    def new_func(*args, **kwargs):
        msg = fn(*args, **kwargs)
        new_msg = 'Time: {}, {}'.format(datetime.now(), msg)
        return new_msg
    return new_func

'''
the important part as below, we are passing the 'greet' to the function 'timeWrapper(fn)'
and 'timeWrapper(fn)' returns the new_func. So now 'greet' point to the 'new_func'
Now, when we call greet, we actually call the new_func
'''
greet = timeWrapper(greet) #greet -> new_func
greet('ma') # new_func('ma')


'''
By definition, a Decorator is a callables which takes a callable and returns a callable. 
A callable can be a few things but let’s not worry about that right now. 
In most cases, a decorator just takes a function, wraps it and returns the wrapped function. 
The wrapped function can access a reference to our original function and call it as necessary. 
In our case 'time_wrapper' is the decorator function 
which takes the 'greet' function and returns the 'new_func' as wrapped function.
'''

import os
import pickle

def cached(cachefile):
    """
    A function that creates a decorator which will use "cachefile" for caching the results of the decorated function "fn".
    """
    def decorator(fn):  # define a decorator for a function "fn"
        def wrapped(*args, **kwargs):   # define a wrapper that will finally call "fn" with all arguments
            # if cache exists -> load it and return its content
            # in this case, we  don't call the 'fn'
            if os.path.exists(cachefile):
                    with open(cachefile, 'rb') as cachehandle:
                        print("using cached result from '%s'" % cachefile)
                        return pickle.load(cachehandle)

            # execute the function with all arguments passed
            res = fn(*args, **kwargs)

            # write to cache file
            with open(cachefile, 'wb') as cachehandle:
                print("saving result to cache '%s'" % cachefile)
                pickle.dump(res, cachehandle)

            return res

        return wrapped

    return decorator   # return this "customized" decorator that uses "cachefile"

#使用pickle模块将数据对象保存到文件import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],         'b': ('string', u'Unicode string'),         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
# Pickle dictionary using protocol
# 0.pickle.dump(data1, output)# Pickle the list using the highest protocol available.pickle.dump(selfref_list, output, -1)
output = open('data.pkl', 'wb')

output.close()

