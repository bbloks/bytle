# Bytle
Toolset for Encoders and Decoders of all sorts. <br/>
Dumping just some stuff now, structure follows...


### Some examples:
#### 1. Base 64 encoding and decoding of numpy arrays
```
form bytle import Bytle
import numpy as np

# create bytle instance
B = Bytle

# create a dummy array
arr = np.array([[1, 2], [3, 4]])

# encode
enc = B.base64_encode(arr, style="utf-8", display=False)

# decode and transform
dec_1 = B.base64_decode(enc, dtype='int64', shape=(2, 2))
dec_2 = B.base64_decode(enc, dtype='int64', shape=(1, 4))
```

#### 2. Serializing to JSON and dump result to file
```
form bytle import JsonEncoder
import json
import numpy as np

# create dummy array
arr = np.random.rand(6, 4)

dumped = json.dumps(arr, cls=JsonEncoder)
with open('output.json', 'w') as f:
    json.dump(dumped, f)
```
