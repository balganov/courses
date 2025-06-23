#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
float calculate_index(string t);

int main(void)
{
    string text = get_string("Text: ");
    int grade = calculate_index(text);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

float calculate_index(string t)
{
    int length = strlen(t);
    float letters = 0.0;
    float words = 0.0;
    float sentences = 0.0;
    float index = 0.0;

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
    index =
        round(0.0588 * letters / (words + 1) * 100 - 0.296 * sentences / (words + 1) * 100 - 15.8);
    return index;
}
