class Operations:
    def say_hi(self, name):
        print('Hi, ', name)

    def say_bye(self, name):
        print('Bye, ', name)

    def default(self, arg):
        print('This operation is not supported.')


if __name__ == '__main__':
    operations = Operations()
    command, argument = input('> ').split()
    getattr(operations, command, operations.default)(argument)


'''
$ python getattr_example.py

> say_hi Jordan
Hi, Jordan

> blah blah
This operation is not supported.

'''
