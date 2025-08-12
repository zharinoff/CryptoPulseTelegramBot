from aiogram import Dispatcher
from typing import Protocol


class IHandler(Protocol):
    def register(self, dp: Dispatcher) -> None: ...
