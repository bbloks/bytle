import sys
import base64
import numpy as np


class Base64:

    @staticmethod
    def base64_encode(array, style="utf-8", display=False):
        encoded = base64.b64encode(array).decode(style)
        if display:
            print(encoded)
        return encoded

    @staticmethod
    def base64_decode(array, dtype, shape):

        if sys.version_info.major == 3:
            array = bytes(array, encoding="utf-8")
        array = np.frombuffer(base64.decodebytes(array), dtype=dtype)
        array = array.reshape(shape)

        return array