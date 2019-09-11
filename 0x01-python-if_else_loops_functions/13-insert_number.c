#include "lists.h"
/**
 * insert_node - Insert number into sorted linked list
 * @head: Double pointer to head
 * @number: Number to place into node
 *
 * Return: Address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	tmp = *head;
	while (tmp != NULL)
	{
	        if (tmp->next != NULL)
		{
			if (tmp->n >= number)
			{
				new->next = *head;
				*head = new;
				break;
			}
			else if (tmp->n <= number && tmp->next->n >= number)
			{
				new->next = tmp->next;
				tmp->next = new;
				break;
			}
		}
		else
		{
			if (tmp->n <= number)
			{
				new->next = tmp->next;
				tmp->next = new;
				break;
			}
		}
		tmp = tmp->next;
	}
	return (new);
}
