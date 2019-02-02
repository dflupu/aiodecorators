# aiodecorators
Function decorators based on asyncio Lock, Semaphore and BoundedSemaphore

## Install
`pip3 install aiodecorators`

## Usage

[asyncio.Lock](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock)
```
from aiodecorators import Lock

@Lock
async def f():
    pass
```

[asyncio.Semaphore](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore)
```
from aiodecorators import Semaphore

@Semaphore(n)
async def f():
    pass
```
[asyncio.BoundedSemaphore](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BoundedSemaphore)
```
from aiodecorators import BoundedSemaphore

@BoundedSemaphore(n)
async def f():
    pass
```
