#!/usr/bin/env python

import setuptools as _setuptools

_setuptools.setup(
    name = "klemmbrett",
    version = "0.4",
    description = "Versatile clipboard manager",
    author = "Michael van Bracht",
    author_email = "michael@wontfix.org",
    url = "https://github.com/wontfix-org/klemmbrett",
    packages = _setuptools.find_packages(),
    scripts = ["scripts/klemmbrett"],
    data_files = [
        ("/etc", ["conf/klemmbrett.conf"]),
        ("/etc/xdg/autostart/", ["conf/klemmbrett-autostart.desktop"]),
        ("share/klemmbrett/", ["data/gtk-paste.svg", "data/gtk-paste2.svg"]),
        ("share/applications/", ["conf/klemmbrett.desktop"]),
    ]
)
