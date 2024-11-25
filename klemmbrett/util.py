#!/usr/bin/env python

import html as _html
import importlib.resources as _ir

try:
    from compiler.consts import CO_GENERATOR
except ImportError:
    # IronPython doesn't have a complier module
    CO_GENERATOR = 0x20


def get_status_icon_filename():
    return str(_ir.files("klemmbrett") / "assets/klemmbrett.png")


def isgenerator(func):
    """ Check if a given function is a generator before calling it """
    try:
        return func.func_code.co_flags & CO_GENERATOR != 0
    except AttributeError:
        return False


def yieldwrap(func, *args, **kwargs):
    """ Ensure that the toplevel function is seen as a generator """
    def wrapped():
        for i in func(*args, **kwargs):
            yield i
    return wrapped


def _strtobool (val):
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    else:
        raise ValueError("invalid truth value %r" % (val,))


def humanbool(value):
    """
        Use distutils.util strtobool to convert various boolean tokens
        like yes, on, no, off etc to a boolean
    """
    return _strtobool(str(value).strip().lower() or 'no')


def load_dotted(name):
    """ Imports and return the given dot-notated python object """
    components = name.split('.')
    path = [components.pop(0)]
    obj = __import__(path[0])
    while components:
        comp = components.pop(0)
        path.append(comp)
        try:
            obj = getattr(obj, comp)
        except AttributeError:
            __import__('.'.join(path))
            try:
                obj = getattr(obj, comp)
            except AttributeError:
                raise ImportError('.'.join(path))
    return obj


def htmlsafe(text):
    """ Escape htmlentities """
    return _html.escape(text)

