def func():
    def _():
        var = 'test'
        return var
    print _()


def func2():
    print "meh"


class Test:
    def func3(self):
        def _():
            return "test"
        print _()
