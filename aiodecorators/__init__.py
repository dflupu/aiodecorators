import asyncio
from functools import wraps


class _Synchronizer():

    def __init__(self, *args, **kwargs):
        self.primitive_cls = None
        self.primitive = None
        self.args = args
        self.kwargs = kwargs

    def __call__(self, f):

        @wraps(f)
        async def wrapper(*args, **kwargs):
            if self.primitive is None:
                self.primitive = self.primitive_cls(*self.args, **self.kwargs)

            async with self.primitive:
                return await f(*args, **kwargs)

        return wrapper


class Semaphore(_Synchronizer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primitive_cls = asyncio.Semaphore


class BoundedSemaphore(_Synchronizer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primitive_cls = asyncio.BoundedSemaphore


class Lock(_Synchronizer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primitive_cls = asyncio.Lock
