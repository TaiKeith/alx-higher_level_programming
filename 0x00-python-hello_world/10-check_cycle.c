#include "lists.h"

/**
 * check_cycle - A function that checks if there is a cycle in a linked list
 * @lists: linked list to check
 *
 * Return 1 if there is a cycle, otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
