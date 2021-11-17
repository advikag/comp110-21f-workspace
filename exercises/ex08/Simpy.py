"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730519109 "


class Simpy:
    """The class Simpy."""
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
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value -= step

    def sum(self) -> float:
        """Delegate this algo to the built in sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, x: Union[float, Simpy]) -> Simpy:
        """Operator overload for Power overload."""
        result: Simpy = Simpy([])
        if isinstance(x, float):
            for value in self.values:
                result.values.append(value ** x)
        else:
            assert len(self.values) == len(x.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** x.values[i])
                i += 1
        return result

    def __eq__(self, p: Union[float, Simpy]) -> list[bool]:
        """Operator overload for equality."""
        result: list[bool] = list()
        if isinstance(p, float):
            for value in self.values:
                if value == p:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(p.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == p.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
    
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for greater than."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                if(value > rhs):
                    result.values.append(value)
                else:
                    result.values.append(rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:        
        """Operator overload for subscription notation."""
        if isinstance(rhs, int):
            x: float = 0.0
            for value in self.values:
                if value == self.values[rhs]:
                    x = value
            return x

        else:
            result: Simpy = Simpy([])
            assert len(self.values) == len(rhs)
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
            return result