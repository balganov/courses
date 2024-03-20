#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
void cipher (string s, int k);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage ./ceasar key\n");
        return 1;
    }
    int l = strlen(argv[1]);
    string input = argv[1];
    for (int i = 0; i < l; i++)
    {
        if (input[0] == '0' || !isdigit(input[i]))
        {
            printf("Usage ./ceasar key\n");
            return 1;
        }
    }

    cipher(get_string("plaintext:  "), atoi(input));

    return 0;
}

void cipher (string s, int k)
{
    for (int i = 0, l = strlen(s); i < l; i++)
    {
        if ((s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= 'a' && s[i] <= 'z'))
        {
            if (isupper[i])
            {
                s[i] = s[i] + (k % 26);
                if (s[i] > 90)
                {
                    s[i] = s[i] -25;
                }
            }
            else
            {
                s[i] = s[i] + (k % 26);
                if (s[i] > 122)
                {
                    s[i] = s[i] -25;
                }
            }
        }
    }
    printf("ciphertext: %s\n",s);
}
