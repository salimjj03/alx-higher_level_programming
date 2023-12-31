#include "lists.h"

/**
 * insert_node - ..
 * @head: ..
 * @number: ..
 * Return: ..
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	tmp = *head;
	if (*head == NULL || (*head)->n >= number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (tmp->next != NULL && tmp->next->n <= number)
		tmp = tmp->next;

	newnode->next = tmp->next;
	tmp->next = newnode;
	return (newnode);
}
