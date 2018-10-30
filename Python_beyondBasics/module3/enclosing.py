# No effect on global
message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        message = 'local'

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)


# Demonstration on the effect on global 'message'
print('global message: ', message)
enclosing()
print('global message: ', message)


# Effect on global
message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)


# Demonstration on the effect on global 'message'
print('global message: ', message)
enclosing()
print('global message: ', message)


# Effect on nonlocal
message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)


# Demonstration on the effect on global 'message'
print('global message: ', message)
enclosing()
print('global message: ', message)