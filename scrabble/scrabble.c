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
    string alph_p = "1111111111223333444445881010";
    string check = word;

    for (int i = 0, le = strlen(check); i < le, i++)
    {
        for (int k = 0, l = strlen(alph_c); k < l; k++)
        {
            if (check[i]==alph_c[k])
            {
                printf("found letter %c on index %i\n",check[i], k);
                return 0;
            }
        }
        return 1;
    }
}
