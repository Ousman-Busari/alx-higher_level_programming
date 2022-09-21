#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

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

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if(!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

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
