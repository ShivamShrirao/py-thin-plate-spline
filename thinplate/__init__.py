
try:
    import torch
    from thinplate.hybrid import *
except ImportError or AttributeError:
    from thinplate.numpy import *

__version__ = '1.0.0'
