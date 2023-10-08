#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - ...
 * @head: ..
 * Return: ...
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp_e;
	int *v, i = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp_e = *head;
	while (tmp_e != NULL)
	{
		i++;
		tmp_e = tmp_e->next;
	}
	v = malloc(sizeof(int) * i);
	tmp_e = *head;
	i = 0;
	while (tmp_e != NULL)
	{
		v[i] = tmp_e->n;
		i++;
		tmp_e = tmp_e->next;
	}
	tmp_e = *head;
	i = i - 1;
	while (tmp_e->next != NULL)
	{
		if (tmp_e->n != v[i])
		{
			free(v);
			return (0);
		}
		tmp_e = tmp_e->next;
		i--;
	}
	free(v);
	return (1);
}
