message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)


# Demonstration that global 'message' is not affected
print('global message: ', message)
enclosing()
print('global message: ', message)
