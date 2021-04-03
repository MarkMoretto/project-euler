// https://docs.python.org/3/extending/extending.html#a-simple-example
/*
Compilation notes:

g++ -I %LocalAppData%\Programs\Spyder\venv\Include simple-math.cxx -o simple_math
*/

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <iostream>



static PyObject * simple_math_system(PyObject * self, PyObject * args) {
    const char * command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}


static PyMethodDef SimpleMathMethods[] = {

    {"system", simple_math_system, METH_VARARGS, "Execute a shell command."}
    
    {NULL, NULL, 0, NULL}
}


// Method table reference
static struct PyModuleDef simplemathmodule = {
    PyModuleDef_HEAD_INIT,
    "simple_math",      /* name of module */
    simple_math_doc,    /* module documentation, may be NULL */
    -1,                 /* name of module */
    SimpleMathMethods
}

PyMODINIT_FUNC PyInit_simple_math(void) {
    return PyModule_Create(&simplemathmodule);
}

int main(nt argc, char * argv[]) {
    wchar_t * program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        std::cout << stderr << "Fatal error: Cannot decode argv[0]" << std::endl;
        exit(1);
    }

    /* Add a built-in module, before Py_Initialize */
    if (PyImport_AppendInittab("simple_math", PyInit_simple_math) == -1) {
        std::cout << stderr << "Error: could not extend in-built modules table" << std::endl;
        exit(1);
    }

    /* Pas argv[0] to Python interpretor */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required.
       If this step fails, it will be a fatal error. */
    Py_Initialize();

    /* 
    Optionally import the module;
    Alternatively, import can be deferred until the embedded script imports it.
    */
    pmodule = PyImport_ImportModule("simple_math");
    if (!pmodule) {
        PyErr_Print();
        std::cout << stderr << "Error: Could not import module `simple_math`." << std::endl;
    }

}