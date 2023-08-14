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
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp = NULL, *next_node = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		temp = slow;
		slow = slow->next;
	}

	while (slow != NULL)
	{
		next_node = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next_node;
	}

	while (prev != NULL)
	{
		if ((*head)->n != prev->n)
		{
			while (temp != NULL)
			{
				next_node = temp->next;
				temp->next = prev;
				prev = temp;
				temp = next_node;
			}
			return (0);
		}
		*head = (*head)->next;
		prev = prev->next;
	}

	while (temp != NULL)
	{
		next_node = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next->node;
	}

	return (1);
}
