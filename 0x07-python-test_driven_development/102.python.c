#include "Python.h"

/**
 * print_python_string - prints information about python strings
 * @p: the input python object
 *
 * Return: Nothing
 */
void print_python_string(PyObject *p)
{
	long unsigned length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	length = ((pyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");
	printf(" length: %lu\n", length);
	printf(" value: %ls\n", PyUnicode_AswideCharString(p, &length));
}
