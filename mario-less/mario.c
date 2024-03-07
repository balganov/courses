#include <stdio.h>
#include <cs50.h>
void draw (int a);

int main(void)
{

    int height;
    do
    {
        height = get_int("Pyramid height: ");
    }
    while (height < 1);

    draw (height);
}

void draw (int a)
{
    for (int r = 0; r < a; r++)
    {
        for (int c = 0; c < a; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}
