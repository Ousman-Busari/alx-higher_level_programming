#include "lists.h"

/**
 * insert_node - insert a number into a sorted linked list
 * @head: pointer to the head of the sorted linked list
 * @number: number to be inserted
 *
 * Return: address of the new node, or NULL, if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *temp1, *new_node;

	new_node = malloc(sizeof(listint_t));
	if(!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		return (NULL);

	if ((*head)->next == NULL && number > (*head)->n)
	{
		(*head)->next = new_node;
		return (new_node);
	}
	else if ((*head)->next == NULL && number < (*head)->n)
	{
		new_node->next = *head;
		return (new_node);
	}
	else if ((*head)->n > number)
	{
		new_node->next = *head;
		return (new_node);
	}

	temp = *head;
	temp1 = (*head)->next;
	while (temp && temp1)
	{
		if (temp->n < number && temp1->n > number)
		{
			temp->next = new_node;
			new_node->next = temp1;
			return (new_node);
		}
		temp = temp1;
		temp1 = temp1->next;
	}
	temp->next = new_node;
	return(new_node);
}
