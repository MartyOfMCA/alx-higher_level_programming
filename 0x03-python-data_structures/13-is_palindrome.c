#include "lists.h"

/**
 * is_palindrome - Determines whether @head
 * points to a list that contains a
 * palindrome.
 *
 * @head: A pointer to the memory address to the
 * head node
 *
 * Return: 1 if the list contains a palindrome
 * otherwise 0
 *
 **/
int is_palindrome(listint_t **head)
{
	listint_t *mid = NULL, *current = NULL, *previous = NULL, *next = NULL;
	int ret_value = 1;

	if ((*head) == NULL)
	{
		return (ret_value);
	}
	mid = *head;
	current = *head;
	while (current->next != NULL && current->next->next != NULL)
	{
		current = current->next->next;
		mid = mid->next;
	}
	current = next = mid;
	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	current = *head;
	while (current->next != NULL)
	{
		if (previous->n != current->n)
		{
			ret_value = 0;
			break;
		}
		current = current->next;
		previous = previous->next;
	}

	return (ret_value);
}
