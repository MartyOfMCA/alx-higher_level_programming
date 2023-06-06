#include "lists.h"

/**
 * insert_node - Add a node to the appropriate position in a sorted list
 *
 * @head: The memory address to the head node
 * @number: The value for the new node to be added
 *
 * Return: The address of the new node or NULL if the operation fails
 *
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *current = NULL, *previous = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	current = *head;
	while (current != NULL)
	{
		if (current->n <= number)
		{
			previous = current;
			current = current->next;
			continue;
		}
		break;
	}
	new_node->n = number;
	new_node->next = current;
	if (previous != NULL)
	{
		previous->next = new_node;
	}
	else
	{
		*head = new_node;
	}
	return (new_node);
}
