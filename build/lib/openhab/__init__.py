"""Module entry point."""

modules = ['']

try:
    from .events import ItemEvent
    modules.extend(['ItemEvent'])
except ImportError:
    print("ItemEvent is not installed")

try:
    from .crud import CRUD
    modules.extend(['CRUD'])
except ImportError:
    print("CRUD is not installed")

try:
    from .item import Item, ColorItem, ContactItem, DateTimeItem, DimmerItem, GroupItem, ImageItem, LocationItem, NumberItem, PlayerItem, RollershutterItem, StringItem, SwitchItem
    modules.extend(['Item', 'ColorItem', 'ContactItem', 'DateTimeItem', 'DimmerItem', 'GroupItem', 'ImageItem', 'LocationItem', 'NumberItem', 'PlayerItem', 'RollershutterItem', 'StringItem', 'SwitchItem'])
except ImportError:
    print("Item is not installed")

__all__ = modules
__version__ = "0.1.1"
__author__ = 'Michael Dörflinger'
__credits__ = 'Furtwangen University'
