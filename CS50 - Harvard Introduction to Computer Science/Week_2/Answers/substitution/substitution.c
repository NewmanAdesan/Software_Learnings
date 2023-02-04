#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool contains_duplicate(string key);
char get_cipher_letter(char letter, string cipher_key);

int main(int argc, string argv[])
{
    // user must input only one command line argument
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // user argument must be a string of 26 letters
    if (strlen(argv[1]) != 26)
    {
        printf("Key must be 26 letters.\n");
        return 1;
    }

    // all characters in user argument must be an alphabeth
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("All key characters must be Alphabeths.\n");
            return 1;
        }
    }

    // user argument must not contain a duplicate character
    if (contains_duplicate(argv[1]))
    {
        printf("key must not contain duplicate characters.\n");
        return 1;
    }

    // saving the key in a variable for better readability
    string key = argv[1];

    // prompting user for plaintext
    string text = get_string("plaintext:  ");

    // printing each charater of the cipher text one at a time on the same line
    printf("ciphertext: ");

    int text_len = strlen(text);

    // loop through each character in the text
    for (int i = 0; i < text_len; i++)
    {
        char cipher_letter = get_cipher_letter(text[i], key);
        printf("%c", cipher_letter);
    }

    printf("\n");
}


bool contains_duplicate(string key)
{
    /* Make a boolean array of length 26
     * representing all the characters.
     * all entries will be initially false
     * if a character is seen, its position entry will become true
     *
     * if the charater is seen again, that would mean its position
     * entry will already be true
     */

    bool already_seen[26];

    for (int i = 0; i < 26; i++)
    {
        already_seen[i] = false;
    }

    for (int i = 0; i < 26; i++)
    {
        char character = key[i];
        character = toupper(character);
        character -= 'A';

        if(already_seen[(int)character] == true)
        {
            return true;
        }

        already_seen[(int)character] = true;
    }

    return false;
}


char get_cipher_letter(char letter, string cipher_key)
{
    // if letter is an alphabeth do this
    if (isalpha(letter))
    {
        // for uppercase letters
        if (isupper(letter))
        {
            // get the letter position on a scale of 0-25
            // converting from scale 65-90 to 0-25
            int scaled_position = letter - 65;

            // the cipher letter will be the letter at scaled_position of the key
            return toupper(cipher_key[scaled_position]);
        }
        // for lowercase letters
        else
        {
            // get the letter position on a scale of 0-25
            // converting from scale 97-122 to 0-25
            int scaled_position = letter - 97;

            // the cipher letter will be the letter at scaled_position of the key
            return tolower(cipher_key[scaled_position]);
        }

    }
    // if letter is not an alphabeth do this
    else
    {
        return letter;
    }
}