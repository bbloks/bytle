from bytle import Bytle
from bytle import JsonEncoder

import numpy as np

B = Bytle

arr = np.array([[1, 2], [3, 4]])
enc = B.base64_encode(arr)


dec = B.base64_decode(enc, dtype='int64', shape=(1, 4))
dec = B.base64_decode(enc, dtype='int64', shape=(2, 2))

import json
arr = np.array([[1, 2], [3, 4]])

dumped = json.dumps(arr, cls=JsonEncoder)
with open('output.json', 'w') as f:
    json.dump(dumped, f)