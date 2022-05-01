# SPDX-License-Identifier: GPL-2.0-or-later

import sys


if sys.platform == "emscripten":

    import vialglue

    class hiddevice:

        def open_path(self, path):
            print("opening {}...".format(path))

        def write(self, data):
            print("WRITE {}".format(data.hex()))
            return vialglue.write_device(data)

        def read(self, length, timeout_ms=0):
            data = vialglue.read_device()
            print("READ {}".format(data.hex()))
            return data


    class hid:

        @staticmethod
        def enumerate():
            return [{'path': b'/pseudo', 'vendor_id': 123, 'product_id': 321, 'serial_number': 'vial:f64c2b3c', 'release_number': 1, 'manufacturer_string': 'vial', 'product_string': 'test', 'usage_page': 65376, 'usage': 97, 'interface_number': 1}]

        @staticmethod
        def device():
            return hiddevice()

elif sys.platform.startswith("linux"):
    import hidraw as hid
else:
    import hid
