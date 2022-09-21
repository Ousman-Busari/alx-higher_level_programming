#include "lists.h"

/**
 * check_cycle - checks if a linked list is circular
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if it's a circular link, 0 if not
 */

int check_cycle(listint_t *head)
{
	listint_t *ap, *gp;

	if (head == NULL || head->next == NULL)
		return (0);

	ap = head->next;
	gp = head->next->next;

	while (gp && gp->next)
	{
		if (ap == gp)
			return (1);
		ap = ap->next;
		gp = gp->next->next;
	}
	return (0);
}
