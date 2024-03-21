#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void cipher(string s, int k);

int main(int argc, string argv[])
{
    bool alpha = true;
    if (argc == 2)
    {
        int l = strlen(argv[1]);
        string input = argv[1];
        for (int i = 0; i < l; i++)
        {
            if (!isalpha(input[i]))
            {
                alpha = false;
            }
        }
    }
    if (argc != 2 || alpha = false)
    {
        printf("Usage ./ceasar key\n");
        return 1;
    }


    cipher(get_string("plaintext:  "), atoi(input));

    return 0;
}

void cipher(string s, int k)
{
    printf("ciphertext: %s\n", s);
}
