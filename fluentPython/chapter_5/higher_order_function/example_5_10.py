# tag generates HTML. A keyword-only argument cls is used to pass
# "class" attributes as a work-around because class is a keyword in Python.

def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                            in sorted(attrs.items()))
    else:
        attr_str = ''
    
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name="imgc"))

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
            'src': 'sunset.jpg', 'cls': 'framed'}

print(tag(**my_tag))