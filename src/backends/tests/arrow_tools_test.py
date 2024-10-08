# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass

import pyarrow as pa
import pytest

from src.backends.arrow_tools import reapply_names


@dataclass
class TestCase:
    name: str
    input: pa.Table
    names: list[str]
    expected: pa.table
    fail: bool = False


cases: list[TestCase] = [
    TestCase('empty table', pa.Table.from_arrays([]), [], pa.Table.from_arrays([])),
    TestCase('too many names', pa.Table.from_arrays([]), ['a', 'b'], pa.Table.from_arrays([]),
             fail=True),
    TestCase('normal columns',
             pa.Table.from_pydict(
                 {"name": [None, "Joe", "Sarah", None], "age": [99, None, 42, None]},
                 schema=pa.schema({"name": pa.string(), "age": pa.int32()})
             ),
             ['renamed_name', 'renamed_age'],
             pa.Table.from_pydict(
                 {"renamed_name": [None, "Joe", "Sarah", None],
                  "renamed_age": [99, None, 42, None]},
                 schema=pa.schema({"renamed_name": pa.string(), "renamed_age": pa.int32()})
             )),
    TestCase('too few names',
             pa.Table.from_pydict(
                 {"name": [None, "Joe", "Sarah", None], "age": [99, None, 42, None]},
                 schema=pa.schema({"name": pa.string(), "age": pa.int32()})
             ),
             ['renamed_name'],
             pa.Table.from_pydict(
                 {"renamed_name": [None, "Joe", "Sarah", None],
                  "renamed_age": [99, None, 42, None]},
                 schema=pa.schema({"renamed_name": pa.string(), "renamed_age": pa.int32()})
             ),
             fail=True),
    TestCase('struct column',
             pa.Table.from_arrays(
                 [pa.array([{"": 1, "b": "b"}],
                           type=pa.struct([("", pa.int64()), ("b", pa.string())]))],
                 names=["r"]),
             ['r', 'a', 'b'],
             pa.Table.from_arrays(
                 [pa.array([{"a": 1, "b": "b"}],
                           type=pa.struct([("a", pa.int64()), ("b", pa.string())]))], names=["r"])
             ),
    # TODO -- Test nested structs.
    # TODO -- Test a list.
    # TODO -- Test a map.
    # TODO -- Test a mixture of complex and simple types.
]


class TestArrowTools:
    """Tests the functionality of the arrow tools package."""

    @pytest.mark.parametrize(
        "case", cases, ids=lambda case: case.name
    )
    def test_reapply_names(self, case):
        failed = False
        try:
            result = reapply_names(case.input, case.names)
        except ValueError as _:
            result = None
            failed = True
        if case.fail:
            assert failed
        else:
            assert result == case.expected

