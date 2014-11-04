#include "Python.h"
#include "hello.h"

static char py_hello_doc[] = "Prints hello world";

static PyObject *
py_hello(PyObject *self)
{
    int r;
    r = hello();
    return Py_BuildValue("i", r);
}

static PyMethodDef hellomethods[] = {
    {'hello', py_hello, NULL, py_hello_doc}
};
 
static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "_hello",
    NULL,
    -1,
    _hellomethods
};

PyMODINIT_FUNC
PyInit__hello(void)
{
    return PyModule_Create(&_hello);
}


