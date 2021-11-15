"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730519109 "


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new simpy object."""
        self.values = values

    def __str__(self) -> str:
        """String representation of a simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill our values array by mutating object called on."""
        self.values = []
        i: int = 0
        while i < times:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the range of values."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Delegate this algo to the built in sum function"""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            for value in self.values:
                result.values.append(value + rhs )
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
   
        return result




