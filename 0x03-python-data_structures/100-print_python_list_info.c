#include "lists.h"

/**
 * print_python_list_info - ..
 * @p: ..
 * Return: ..
 */

void print_python_list_info(PyObject *p)
{
	PyObject *list;
	Py_ssize_t l_size;
	int i = 0;

	if (PyList_Check(p) == 1)
	{
		l_size = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", l_size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		while (i  < l_size)
		{
			list = PyList_GetItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(list)->tp_name);
			i++;
		}
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "Object is not a list");
		return;
	}
}
