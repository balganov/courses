#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
void points (string word);

int main(void)
{
    string player1, player2;


    player1 = get_string("Player 1: ");
    player2 = get_string("Player 2: ");

    points(player1);
    //points(player2);
}

void points (string word)
{
    string alph_c = "AEILNORSTUDGBCMPFHVWYKJXQZ";
    int alph_p[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 8, 8, 10, 10};
    int points = 0;

    for (int i = 0, l1 = strlen(word); i < l1; i++)
    {
        word[i] = toupper(word[i]);
        for (int k = 0, l2 = strlen(alph_c); k < l2; k++)
        {
            if (word[i] == alph_c[k])
            {
                printf("found letter %c on index %i\n",word[i], k);
                points += alph_p[k];
            }
        }
    }
    printf("points = %i\n",points);
}
