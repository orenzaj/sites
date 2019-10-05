try:
    from settings.base import *
except ImportError as err:
    print("No settings/base.py found.")
    pass

try:
    from settings.local import *
except ImportError as err:
    print("No settings/local.py found.")
    pass
