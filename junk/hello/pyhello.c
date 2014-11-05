#include "Python.h"
#include "hello.h"

static char py_hello_doc[] = "Prints hello world";

static PyObject *
py_hello(PyObject *self, PyObject *args)
{
    int r;

    r = hello();
    return Py_BuildValue("i", r);
}

/* 1st field is method name internal to python, 2nd field is the
 * py_wrapper, 3rd field indicates tuple of args are being passed */
static PyMethodDef hellomethods[] = {
    {"hello", py_hello, METH_NOARGS, py_hello_doc},
    {NULL, NULL, 0, NULL}, /* Sentinel */
};

/* 2nd field is ModuleName, 3'rd is doc string */
static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "_hello",
    py_hello_doc,
    -1,
    hellomethods
};

/* PyInit_ModuleName(... */
PyMODINIT_FUNC
PyInit__hello(void)
{
    return PyModule_Create(&hellomodule);
}


