#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

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

    printf("all good %s", argv[1]);
}
