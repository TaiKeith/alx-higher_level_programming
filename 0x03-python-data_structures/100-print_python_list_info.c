#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - A function that prints some basic info about
 * python lists
 * @p: A pointer to a python list object
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyListObject *obj = NULL;

	obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %li: %s\n", i, Py_TYPE(obj_item[i]->tp_name));
	}
}
