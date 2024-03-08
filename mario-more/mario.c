#include <cs50.h>
#include <stdio.h>
void draw(int a);

int main(void)
{

    int height;

    do
    {
        height = get_int("Pyramid height: ");
    }
    while (height < 1);

    draw(height);
}

void draw(int a)
{
    int b = a - 1;
    for (int i = 0; i < a; i++)
    {
        for (int k = 0; k < b - i; k++)
        {
            printf(" ");
        }
        for (int j = 0; j < i + 2; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
