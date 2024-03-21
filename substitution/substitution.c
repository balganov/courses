#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void cipher(string s, int k);

int main(int argc, string argv[])
{
    bool alpha = true;
    int l = 0;
    string input = "";
    if (argc == 2)
    {
        l = strlen(argv[1]);
        input = argv[1];
        for (int i = 0; i < l; i++)
        {
            if (!isalpha(input[i]) || strchr("ABCDEFGHIJKLMNOPQRSTUVWXYZ",input[i]) == NULL)
            {
                alpha = false;
                break;
            }
        }
    }
    else
    {
        printf("Usage ./substitution key\n");
        return 1;
    }

    if (alpha == false || l != 26)
    {
        printf("there is an error\n");
        return 1;
    }


    cipher(get_string("plaintext:  "), atoi(input));

    return 0;
}

void cipher(string s, int k)
{
    printf("ciphertext: %s\n", s);
}
