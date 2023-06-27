#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Print the size and memory
 * allocated for a list including its elements type.
 *
 * @p: A pointer to the list object to be examined
 *
 **/
void print_python_list(PyObject *p)
{
	Py_ssize_t list_size = 0, index = 0;

	list_size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	while (index < list_size)
	{
		printf("Element %ld: %s\n", index,
		(PyList_GET_ITEM(p, index)->ob_type)->tp_name);
		if (PyBytes_Check(PyList_GET_ITEM(p, index)))
		{
			print_python_bytes(PyList_GET_ITEM(p, index));
		}
		index++;
	}
}

/**
 * print_python_bytes - Print byte object on a list.
 *
 * @p: A pointer to the list object to be examined
 *
 **/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t byte_size = 0, index = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		byte_size = PyBytes_Size(p);
		printf("  size: %ld\n", byte_size);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		byte_size++;
		byte_size = byte_size > 10 ? 10 : byte_size;
		printf("  first %ld bytes:", byte_size);
		while (index < byte_size)
		{
			printf(" %02x", PyBytes_AsString(p)[index]);
			index++;
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}

}
