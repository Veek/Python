from distutils.core import setup, Extension
setup(name="hello",
      version = '1.0',
      py_modules = ['hello.py'],
      ext_modules = [
        Extension("_hello",
                  sources=["pyhello.c", "hello.c"],
                  depends=["hello.h"])
    ]
)
