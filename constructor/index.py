#acess specifier allows us to manage the visibilty and acessibilty of class  atributes
#in python there no true acess specifier like jave , c++ and c#
class hello:
    def __init__(self):
        print("this is a constructor")
        self.__hi()

    def _ok(self):
        print("this is a protected function")

    def __hi(self):
        print("this is a private function")

i=hello()
#i.__init__()
i._ok()
