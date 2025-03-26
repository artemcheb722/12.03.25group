import base64

encoded = base64.b64encode(b"Hello")
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)