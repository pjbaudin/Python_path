def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


# Add decorator
@escape_unicode
def chinese_char():
    return '一二三'
