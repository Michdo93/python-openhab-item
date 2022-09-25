"""Module entry point."""

modules = ['']

try:
    from .events import ItemEvent
    modules.extend(['ItemEvent'])
except ImportError:
    print("python-openhab-itemevent is not installed")

try:
    from .crud import CRUD
    modules.extend(['CRUD'])
except ImportError:
    print("python-openhab-crud is not installed")

try:
    from .item import Item, ColorItem, ContactItem, DateTimeItem, DimmerItem, GroupItem, ImageItem, LocationItem, NumberItem, PlayerItem, RollershutterItem, StringItem, SwitchItem
    modules.extend(['Item', 'ColorItem', 'ContactItem', 'DateTimeItem', 'DimmerItem', 'GroupItem', 'ImageItem', 'LocationItem', 'NumberItem', 'PlayerItem', 'RollershutterItem', 'StringItem', 'SwitchItem'])
except ImportError:
    print("python-openhab-item is not installed")

try:
    from .logsaver import LogReader, LogSaver
    modules.extend(['LogReader', 'LogSaver'])
except ImportError:
    print("python-openhab-logsaver is not installed")

try:
    from .eventbus import EventBus
    modules.extend(['EventBus'])
except ImportError:
    print("python-openhab-eventbus is not installed")

__all__ = modules
__version__ = "1.0.0"
__author__ = 'Michael Dörflinger'
__credits__ = 'Furtwangen University'
