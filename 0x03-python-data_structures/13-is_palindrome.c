#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - A function that checks if a linked list is a palindrome
 * @head: Pointer to the head of the linked list
 *
 * Return: 1 if it's a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	/*Move slow to the middle, and reverse the second half*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
