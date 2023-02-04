#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

// Prototypes
int only_digits(char *input);

int main(int argc, char *argv[]) 
{
    // user must input only one argument, else wrong input
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // users input must only be digits
    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // convert string input into an integer
    int key = atoi(argv[1]);

    // prompting user for plaintext
    // printf("plaintext:  ");
    // string plaintext = get_string("plaintext:  ");

    char *plaintext = "HELLO, WORLD";
    int text_len = strlen(plaintext);

    // printing the cipher text
    printf("ciphertext: ");

    for (int i = 0; i < text_len; i++)
    {
        // how to cipher alphabeths
        if (isalpha(plaintext[i]))
        {   
            // depending on if alphabeth is lowercase or upper case, this value changes
            int scale;

            // how to cipher upper case letters of the alphabeth
            if (isupper(plaintext[i]))
            { 
                scale = 65; 
            }

            // how to cipher lower case letters of the alphabeth
            else
            { 
                scale = 97; 
            }

            //take the scale from 65-90(A-Z) OR 97-122(a-z) to 0-25
            int scaled_letter = plaintext[i] - scale;

            // get the cipher based on the key
            int scaled_cipher = (scaled_letter + key) % 26;

            // take the scale back from 0-25 to 65-90 OR 97-122
            char cipher = scaled_cipher + scale;

            // print the cipher without a new line
            printf("%c", cipher);
        }

        // how to cipher non-alphabeths
        else
        {
            printf("%c", plaintext[i]);
        }
    
    }

    printf("\n");




}

int only_digits(char *input)
{
    // getting the length of user input
    int len = strlen(input);

    // All character in users input string must be numeric
    for (int i = 0; i < len; i++)
    {
        if (input[i] < '0' || input[i] > '9')
        {
            return 0;
        }
    }

    // when user input is correct
    return 1;
}