import base64

text = "Hello everyone"

text = text.encode("ascii")

text_b64 = base64.b64encode(text)

print(text_b64)