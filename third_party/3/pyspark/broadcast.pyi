# Stubs for pyspark.broadcast (Python 3.5)
#

import threading
from typing import Any, Generic, Optional, TypeVar

T = TypeVar('T')

class Broadcast(Generic[T]):
    def __init__(self, sc: Optional[Any] = ..., value: Optional[T] = ..., pickle_registry: Optional[Any] = ..., path: Optional[Any] = ...) -> None: ...
    def dump(self, value, f): ...
    def load(self, path): ...
    @property
    def value(self) -> T: ...
    def unpersist(self, blocking: bool = ...) -> None: ...
    def destroy(self) -> None: ...
    def __reduce__(self): ...

class BroadcastPickleRegistry(threading.local):
    def __init__(self) -> None: ...
    def __iter__(self) -> None: ...
    def add(self, bcast: Any) -> None: ...
    def clear(self) -> None: ...
