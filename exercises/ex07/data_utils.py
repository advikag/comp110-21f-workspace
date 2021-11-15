"""Utility functions."""

__author__ = "730519109"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()

    return result


def column_values(t: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] in a single column."""
    ans: list[str] = []
    for i in t:
        result: str = i[column]
        ans.append(result)

    return ans


def columnar(row: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    ans: dict[str, list[str]] = {}
    
    first: dict[str, str] = row[0]
    for column in first:
        ans[column] = column_values(row, column)

    return ans


def head(columnt: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Produce a new column based table."""
    ans: dict[str, list[str]] = {}
    for column in columnt:
        first: list[str] = list()
        if num >= len(columnt[column]):
            return columnt
        else:
            i: int = 0
            while i < num:
                first.append(columnt[column][i])
                i += 1
        ans[column] = first

    return ans


def select(columnt: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a new column."""
    ans: dict[str, list[str]] = {}
    
    for i in name:
        ans[i] = columnt[i]

    return ans


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table."""
    ans: dict[str, list[str]] = {}

    for column in a:
        ans[column] = a[column]
    for column in b:
        if column in ans:
            for i in b[column]:
                ans[column].append(i)
        else:
            ans[column] = b[column]

    return ans


def count(a: list[str]) -> dict[str, int]:
    """Produce a dict with unique key."""
    ans: dict[str, int] = {}
    for i in a:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    return ans
