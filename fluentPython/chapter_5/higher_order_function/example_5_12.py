# Function to shorten a string by clipping at a space near the desired
# length
from inspect import signature

def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
    if space_before >= 0:
        end = space_before
    else:
        space_after = text.rfind(' ', max_len)
    if space_after >= 0:
        end = space_after
    if end is None: # no spaces were found
        end = len(text)
    return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)


# Extracting the function signature.

sig = signature(clip)
print(sig)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)