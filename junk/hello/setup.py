from distutils.core import setup, Extension
setup(name="hello",
      version = '1.0',
      py_modules = ['hello.py'],
      ext_modules = [
        Extension("_hello",
<<<<<<< HEAD
                  sources = ["pyhello.c", "hello.c"],
                  depends = ["hello.h"])
=======
                  sources=["pyhello.c", "hello.c"],
                  depends=["hello.h"])
>>>>>>> 6fc66807824281f810825dad33af9c41653598b0
    ]
)
