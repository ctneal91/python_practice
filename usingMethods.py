class files:

    def __init__(self,value):
        self._v=value
        print("constructor")
    def move(self):
        print("move data",self._v)
    def copy(self):
        print("copy data",self._v)
    def delete(self):
        print("delete data",self._v)

def main():

    mktg=files(99)
    mktg.move()
    mktg.copy()
    mktg.delete()

    exam=files(77)
    exam.move()
    exam.copy()
    exam.delete()

main()
