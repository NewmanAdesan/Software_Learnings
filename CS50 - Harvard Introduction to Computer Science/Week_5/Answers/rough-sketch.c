

#include <stdlib.h>
#include <stdio.h> 

#define N 5

int array[N];

typedef struct node *nodePtr;

struct node {
	int number;
	nodePtr next;
};

typedef struct node node;


int main()
{
	for (int i = 1; i <= N; i++)
	{
		array[i-1] = i;
	}


	nodePtr list = malloc(sizeof(node));
	list -> number = array[0];
	list -> next = NULL;

	nodePtr listCursor = list;

	for (int i = 1; i < N; i++)
	{
		listCursor->next = malloc(sizeof(node));
		listCursor->next->number = array[i];

		if (i == N-1) listCursor->next->next = list;
		else listCursor->next->next = NULL;

		listCursor = listCursor->next;

	}	
}



