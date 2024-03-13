#include <cs50.h>
#include <stdio.h>
int get_length(long a);
int get_first_digit (long a);

int main(void)
{
    long card_number;

    do
    {
        card_number = get_long("Number: ");
    }
    while (card_number < 0);

    int second_to_last;
    int last = card_number % 10;
    int sum = 0;
    int length = get_length(card_number);
    int first_digit = get_first_digit(card_number);
    int first_two_digits = get_first__two_digits(card_number);
    //5555555555554444
    for (long i = 10; i < 1000000000000000000; i=i*100)
    {
        second_to_last = (card_number/i % 10)*2;
        //printf("second to last %i\n",second_to_last);
        if (second_to_last < 9)
        {
            sum = sum + (card_number/i % 10)*2;
        } else
        {
            sum = sum + second_to_last%10 + 1;
        }
        //printf("sum inside first loop %i\n",sum);
    }

    for (long i = 100; i < 10000000000000000; i=i*100)
    {
        last = last + card_number/i % 10;
        //printf("last inside second loop %i\n",last);
    }

    if ((sum + last) % 10 == 0)
    {
        if (first_digit == 3 && length == 15) printf("AMEX\n");
        if (first_digit == 4 && (length == 13 || length == 16)) printf("VISA\n");
        if (first_digit == 5 && length == 16) printf("MASTERCARD\n");
    } else
    {
        printf("INVALID\n");
    }
}

int get_length (long a)
{
    int i = 1;
    while (a > 9)
    {
        a /= 10;
        i++;
    }
    return i;
}
int get_first_digit (long a)
{
    while (a > 9)
    {
        a /= 10;
    }
    return a;
}
int get_first_two_digits (long a)
{
    while (a > 90)
    {
        a /= 10;
    }
    return a;
}
