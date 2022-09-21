#include "lists.h"

/**
 * check_cycle - checks if a linked list is circular
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if it's a circular link, 0 if not
 */

int check_cycle(listint_t *head)
{
	listint_t **arr = NULL, *temp = NULL;
	int i = 0, j;

	temp = head;
	while (temp)
	{
		i++;
		arr = create_arr_of_list(head, i);
		temp = temp->next;
		for (j = 0; j < i; j++)
		{
			if (temp == arr[j])
			{
				free(arr);
				return (1);
			}
		}
		free(arr);
	}
	return (0);
}


/**
 * create_arr_of_list - create an arr from a linked list
 * @head: pointer to the head of the linked list
 * @n: number of elements to be added to the array
 *
 * Return: pointer to the array of nodes linked list
 */

listint_t **create_arr_of_list(listint_t *head, int n)
{
	int i = 0;
	listint_t **arr;

	if (head == NULL)
		return (NULL);
	arr = malloc(sizeof(listint_t *) * n);
	if (!arr)
		return (NULL);

	for (i = 0; i < n && head; i++)
	{
		arr[i] = head;
		head = head->next;
	}
	return (arr);
}
