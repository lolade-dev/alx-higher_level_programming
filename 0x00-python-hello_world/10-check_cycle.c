#include "lists.h"
/**
 * check_cycle - checks of a singly linked list has a cycle in it
 * @list: linked list to check
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *small = list;
	listint_t *big = list;

	if (list == NULL)
		return (0);
	while (small && big && big->next)
	{
		small = small->next;
		big = big->next->next;
		if (small == big)
			return (1);
	}
	return (0);
}
