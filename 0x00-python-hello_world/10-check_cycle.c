#include "lists.h"

/**
 * check_cycle - ...
 * @list: ...
 * Return: ..
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	if (list == NULL || list->next == NULL)
		return (0);

	ptr1 = ptr2 = list;
	while (ptr1 != NULL && ptr2 != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
