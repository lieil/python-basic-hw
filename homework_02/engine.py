"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    """Class for vehicle props"""
    volume: int
    pistons: int
