#include "lists.h"
/**
 * check_cycle - Check if linked list has a cycle
 * @list: Pointer to head of list
 *
 * Return: 1 if cycle found or 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *next;

	current = list;
	next = list;
	while (current && next && next->next)
	{
		current = current->next;
		next = next->next->next;
		if (current == next)
		{
			return (1);
		}
	}
	return (0);
}
