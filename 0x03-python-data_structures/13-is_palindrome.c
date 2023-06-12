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
	listint_t *node;
	int ret_value = 0;
	int str_len = 0, index = 0, null_byte = 1, itoa_index = 0;
	char *str = NULL, *_itoa = NULL;

	if (*head == NULL)
	{
		return (1);
	}
	node = *head;
	while (node != NULL)
	{
		_itoa = _itostr(node->n);
		str_len += _strlen(_itoa);
		str_len++;
		free(_itoa);
		node = node->next;
	}
	str_len--;
	node = *head;
	str = malloc(sizeof(char) * (str_len + null_byte));
	while (node != NULL)
	{
		_itoa = _itostr(node->n);
		itoa_index = 0;
		while (_itoa[itoa_index] != '\0')
			str[index++] = _itoa[itoa_index++];
		if (node->next != NULL)
			str[index++] = ',';
		free(_itoa);
		node = node->next;
	}
	str[index] = '\0';
	ret_value = _strtkcmp(str);
	free(str);
	return (ret_value);
}

/**
 * _itostr - Converts the given number to a string
 * representation to be manipulated.
 *
 * @number: The number to be converted
 *
 * Return: A string representation for @number
 *
 **/
char *_itostr(int number)
{
	int dup_number = 0, index = 0, tokens = 0, null_byte = 1;
	char *str = NULL;

	dup_number = number;
	if (dup_number < 0)
	{
		tokens++;
		dup_number *= -1;
	}
	while (dup_number > 0)
	{
		tokens++;
		dup_number /= 10;
	}
	if (number == 0)
	{
		str = malloc(sizeof(char) * 1 + null_byte);
		str[index++] = '0';
	}
	else
	{
		str = malloc(sizeof(char) * tokens + null_byte);
	}
	if (number < 0)
	{
		str[index++] = '-';
		number *= -1;
	}
	while (index < tokens)
	{
		str[index] = (number % 10) + '0';
		number /= 10;
		index++;
	}
	str[index] = '\0';

	return (str);
}

/**
 * _strtkcmp - Tokenize the given string and compares
 * elements lexicographically.
 *
 * @str: The given string
 *
 * Return: 1 when the given string is a palindrome
 * otherwise 0
 *
 **/
int _strtkcmp(char *str)
{
	char **tokens = NULL;
	char *token = NULL;
	int token_count = 0, index = 0, null_element = 1;
	int ret_value = 1;

	while (str[index] != '\0')
	{
		if (str[index] == ',')
		{
			token_count++;
		}
		index++;
	}
	token_count++;
	tokens = malloc(sizeof(char *) * (token_count + null_element));
	index = 0;
	token = strtok(str, ",");
	tokens[index++] = token;
	while (token != NULL)
	{
		token = strtok(NULL, ",");
		tokens[index] = token;
		index++;
	}
	index = 0;
	token_count--;
	while (index < token_count)
	{
		if (strcmp(tokens[index], tokens[token_count]))
		{
			ret_value = 0;
			break;
		}
		index++;
		token_count--;
	}
	free(tokens);

	return (ret_value);
}

/**
 * _strlen - Obtain the number of characters in the
 * given string.
 *
 * @str: The given string
 *
 * Return: The size for @str ignoring the null byte
 *
 **/
int _strlen(char *str)
{
	int str_len = 0;

	while (str[str_len] != '\0')
	{
		str_len++;
	}

	return (str_len);
}
