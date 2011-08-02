from sst.actions import *
from time import time

CALLS = 0
def get_condition(result=True, wait=0, raises=False,
                  cond_args=None, cond_kwargs=None):
    initial = time()
    def condition(*args, **kwargs):
        global CALLS
        CALLS += 1
        if cond_args is not None:
            if cond_args != args:
                # can't raise an assertion error here!
                raise TypeError('wrong args passed')
        if cond_kwargs is not None:
            if cond_kwargs != kwargs:
                # can't raise an assertion error here!
                raise TypeError('wrong args passed')
        if time() > initial + wait:
            return result
        if raises:
            raise AssertionError('not yet')
        return False
    return condition

goto('/')
set_wait_timeout(1)

waitfor(get_condition(True))
fails(waitfor, get_condition(False))

waitfor(get_condition(raises=True))
fails(waitfor, get_condition(False, raises=True))

waitfor(url_is, '/')
fails(waitfor, url_is, '/thing')

waitfor(url_is, url='/')
fails(waitfor, url_is, url='/thing')

CALLS = 0
fails(waitfor, get_condition(wait=2))
assert CALLS > 6

fails(waitfor, get_condition(wait=2, raises=True))

set_wait_timeout(5)
waitfor(get_condition(wait=2))
waitfor(get_condition(wait=2, raises=True))

set_wait_timeout(3, 1)
CALLS = 0
waitfor(get_condition(wait=2))
assert CALLS <= 3

