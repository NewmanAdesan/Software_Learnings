#include <cs50.h>
#include <stdio.h>

int check_length(long card_number);
int check_checksum(int card_length);
int check_card_type(int card_length);

int main(void) 
{
    // get the card number from the user
    long number = get_long("Enter Card Number: ");

    // check card length

    // valid or invalid. valid card length are either 
    // 13, 14, 15, 16. other than that print invalid 
    // and exit loop (return 1).

    // check checksum using luhn algorithm

    // if invalid, print INVALID, return 1

    // check card type, VISA<1>, AMERICAN EXPRESS<2>, <MASTER CARD>
    
}