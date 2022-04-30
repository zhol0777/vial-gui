# SPDX-License-Identifier: GPL-2.0-or-later

import sys


if sys.platform == "emscripten":

    import js

    class hid:

        @staticmethod
        def enumerate():
            return js.hid_enumerate()

elif sys.platform.startswith("linux"):
    import hidraw as hid
else:
    import hid
