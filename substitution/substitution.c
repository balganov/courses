#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void cipher(string s, string key);

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
            input[i] = toupper(input[i]);
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


    cipher(get_string("plaintext:  "), input);

    return 0;
}

void cipher(string s, string key)
{
    string a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (int i = 0, l = strlen(s); i < l; i++)
    {
        for (int k = 0, l2 = strlen(a); k < l2; k++)
        {
            if (toupper(s[i]) == a[k])
            {
                if (isupper(s[i]))
                {
                    s[i] = key[k];
                    break;
                }
                else
                {
                    s[i] = tolower(key[k]);
                    break;
                }
            }
        }
    }
    printf("ciphertext: %s\n", s);
}
