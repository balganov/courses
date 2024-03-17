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
    string p1 = "AEILNORSTU";
    string p2 = "DG";
    string p3 = "CMP";
    string p4 = "FHVWY";
    string p5 = "K";
    string p8 = "JX";
    string p10 = "QZ";

    int size = 26;
    string alph[] = {"AEILNORSTUDGBCMPFHVWYKJXQZ","1111111111223333444445881010"};

    printf(alph[0][2]);

        //toupper(word[i])
        printf("\n");
    //return 0;
}
