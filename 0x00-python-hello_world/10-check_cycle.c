#include "lists.h"

/**
 * check_cycle - Determines whether the given list has a
 * cycle or not.
 *
 * @list: A pointer to the list to be traversed
 *
 * Return: 0 should @list have no cycles and 1 should
 * @list have a cycle.
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_node;
	listint_t *fast_node;

	slow_node = list;
	fast_node = list;

	while (fast_node != NULL && fast_node->next != NULL)
	{
		if (fast_node->next == slow_node)
		{
			return (1);
		}
		fast_node = fast_node->next->next;
		slow_node = slow_node->next;
	}
	return (0);
}
