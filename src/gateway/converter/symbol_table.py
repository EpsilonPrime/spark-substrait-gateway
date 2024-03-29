# SPDX-License-Identifier: Apache-2.0
"""Routines to convert SparkConnect plans to Substrait plans."""
import dataclasses
from typing import Optional, List, Dict


@dataclasses.dataclass
class PlanMetadata:
    """Tracks various information about a specific plan id."""
    plan_id: int
    type: Optional[str]
    parent_plan_id: Optional[int]
    input_fields: List[str]  # And maybe type
    generated_fields: List[str]
    output_fields: List[str]

    def __init__(self, plan_id: int):
        self.plan_id = plan_id
        self.symbol_type = None
        self.parent_plan_id = None
        self.input_fields = []
        self.generated_fields = []
        self.output_fields = []


class SymbolTable:
    """Manages metadata related to symbols and provides easy lookup."""
    _symbols: Dict[int, PlanMetadata]

    def __init__(self):
        self._symbols = {}

    # pylint: disable=E1101
    def add_symbol(self, plan_id: int, parent: Optional[int], symbol_type: Optional[str]):
        """Creates a new symbol and returns it."""
        symbol = PlanMetadata(plan_id)
        symbol.symbol_type = symbol_type
        symbol.parent_plan_id = parent
        self._symbols[plan_id] = symbol
        return symbol

    def get_symbol(self, plan_id: int) -> Optional[PlanMetadata]:
        """Fetches the symbol with the requested plan id."""
        return self._symbols.get(plan_id)
