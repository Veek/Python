#include "Python.h"
#include "hello.h"

static char py_hello_doc[] = "Prints hello world";

static PyObject *
py_hello(PyObject *self, PyObject *args)
{
    int x, r;
    if (!PyArg_ParseTuple(args, "i", &x))
        return NULL;

    r = hello(x);
    return Py_BuildValue("i", r);
}

static PyMethodDef hellomethods[] = {
    {"hello", py_hello, METH_VARARGS, py_hello_doc},
    {NULL, NULL, 0, NULL}, /* Sentinel */
};

static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "_hello",
    py_hello_doc,
    -1,
    hellomethods
};

PyMODINIT_FUNC
PyInit__hello(void)
{
    return PyModule_Create(&hellomodule);
}


