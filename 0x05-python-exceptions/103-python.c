#!/usr/bin/python3
#include <stdio.h>
#include <Python.h>


// Function prototypes
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print basic information about Python lists.
 * @p: A PyObject representing a list object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t list_size, list_alloc, i;
    const char *element_type;
    PyListObject *list_object = (PyListObject *)p;
    PyVarObject *var_object = (PyVarObject *)p;

    list_size = var_object->ob_size;
    list_alloc = list_object->allocated;

    fflush(stdout);

    printf("[*] Python list info\n");

    if (strcmp(p->ob_type->tp_name, "list") != 0)
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", list_alloc);

    for (i = 0; i < list_size; i++)
    {
        element_type = list_object->ob_item[i]->ob_type->tp_name;
        printf("Element %ld: %s\n", i, element_type);
        if (strcmp(element_type, "bytes") == 0)
            print_python_bytes(list_object->ob_item[i]);
        else if (strcmp(element_type, "float") == 0)
            print_python_float(list_object->ob_item[i]);
    }
}

/**
 * print_python_bytes - Print basic information about Python byte objects.
 * @p: A PyObject representing a byte object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t byte_size, i;
    PyBytesObject *byte_object = (PyBytesObject *)p;

    fflush(stdout);

    printf("[.] bytes object info\n");

    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", byte_object->ob_sval);

    if (((PyVarObject *)p)->ob_size >= 10)
        byte_size = 10;
    else
        byte_size = ((PyVarObject *)p)->ob_size + 1;

    printf("  first %ld bytes: ", byte_size);
    for (i = 0; i < byte_size; i++)
    {
        printf("%02hhx", byte_object->ob_sval[i]);
        if (i == (byte_size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_float - Print basic information about Python float objects.
 * @p: A PyObject representing a float object.
 */
void print_python_float(PyObject *p)
{
    char *float_buffer = NULL;

    PyFloatObject *float_object = (PyFloatObject *)p;

    fflush(stdout);

    printf("[.] float object info\n");

    if (strcmp(p->ob_type->tp_name, "float") != 0)
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    float_buffer = PyOS_double_to_string(float_object->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", float_buffer);
    PyMem_Free(float_buffer);
}
