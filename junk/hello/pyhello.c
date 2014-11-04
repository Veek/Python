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
    {"hello", py_hello, METH_NOARGS, py_hello_doc},
    {NULL},
};
 
static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "hello",
    NULL,
    -1,
    hellomethods
};

PyMODINIT_FUNC
PyInit__hello(void)
{
    return PyModule_Create(&hellomodule);
}


