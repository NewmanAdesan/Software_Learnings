#include <cs50.h>
#include <stdio.h>

// Prototype
int get_height();

int main(void) 
{
    int height = get_height();


	// think about it, for each line 
	// I am going to print on a line
	// "x number of spaces" 			// first set of spaces
	// then "y number of hashtag" 		// first set of hashtag
	// then "two spaces", 				// second set of spaces constant spaces (2)
	// then "y number of hashtag"		// second set of hashtag


	// loop for each line
    for(int i = 0; i < height; i++)
    {

    	// first set of spaces
    	for(int n_space = 0; n_space < height-(i+1); n_space++ ){
    		printf("%c", ' ');
    	}

    	// first set of hashtag
    	for(int n_hash = 0; n_hash < (i+1); n_hash++ ){
    		printf("%c", '#');
    	}

    	// second set of spaces constant spaces (2)
    	printf("%c%c", ' ', ' ');


    	// second set of hashtag
    	for(int n_hash = 0; n_hash < (i+1); n_hash++ ){
    		printf("%c", '#');
    	}
    	

    	printf("\n");
    	

    }
}

int get_height()
{
	int h;

	do{
		int h = get_int();
	}while(h < 1 || h > 8);

	return h;
}


