#include <Python.h>

void print_python_list_info(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    PyVarObject *varObj = (PyVarObject *)p;

    printf("[*] Size of the Python List = %ld\n", varObj->ob_size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (Py_ssize_t i = 0; i < varObj->ob_size; ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}
