import os as _os

import klemmbrett.util as _util

def newline_to_comma(options, plugin):
    return lambda: plugin.history.top.strip().replace("\n", ",")

def fswalker(options, plugin):
    def walk(base = None):
        if base is None:
            base = options.get("base", _os.getenv("HOME"))

        for item in _os.listdir(base):
            if item.startswith("."):
                continue

            path = _os.path.join(base, item)
            if _os.path.isfile(path):
                yield (item, path)
            elif _os.path.isdir(path):
                yield (item, _util.yieldwrap(walk, path))

    return walk
