#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int points (string word);

int main(void)
{
    string player1, player2;


    player1 = get_string("Player 1: ");
    player2 = get_string("Player 2: ");

    points(player1);
    points(player2);
}

int points (string word)
{
    string p1 = "AEILNORSTU";
    string p2 = "DG";
    string p3 = "CMP";
    string p4 = "FHVWY";
    string p5 = "K";
    string p8 = "JX";
    string p10 = "QZ";

    string alph [size][size] = {}

    for (int i = 0, length = strlen(word); i < length; i++)
    {
        tolower(word[i])
    }
    return 0;
}
