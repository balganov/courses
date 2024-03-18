#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
void calculate_index(string t);

int main(void)
{
    string text = get_string("Text: ");

    calculate_index(text);
}

void calculate_index(string t)
{
    int length = strlen(t);
    int letters = 0;
    int words = 0;
    int sentences = 0;

    for (int i = 0; i < length; i++)
    {
        t[i] = toupper(t[i]);
        if (t[i] >= 'A' && t[i] <= 'Z')
        {
            letters += 1;
        }
        if (t[i] == ' ')
        {
            words += 1;
        }
        if (t[i] == '.' || t[i] == '?' || t[i] == '!')
        {
            sentences += 1;
        }

    }
    printf("number of letters %i\n",letters);
    printf("number of words %i\n",words+1);
    printf("number of sentences %i\n",sentences);
}
