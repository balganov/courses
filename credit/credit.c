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
    //4003600000000014
    int second_to_last = (card_number/10 % 10)*2;
    int last = card_number % 10;
    int sum = second_to_last;
    int length = get_length(card_number);
    int first_digit = get_first_digit(card_number);

    printf("before loop sum %i and length %i and first digit %i \n",sum, length, first_digit);

    for (long i = 1000; i < 10000000000000000; i=i*100)
    {
        second_to_last = (card_number/i % 10)*2;
        if (second_to_last < 9)
        {
            sum = sum + (card_number/i % 10)*2;
        } else
        {
            sum = sum + sum%10 + 1;
        }
        printf("%i in the loop %i\n",second_to_last,sum);
    }

    for (long i = 100; i < 10000000000000000; i=i*100)
    {
        last = last + card_number/i % 10;
        printf("in the second loop %i\n",last);
    }
    printf("afer the loop %i\n",sum);
    //printf("VISA CHECK %li\n",card_number/1000000000000000 % 10);
    if ((sum + last) % 10 == 0)
    {
        if (first_digit == 4 && (length == 13 || length = 16)) printf("VISA\n");
        if (first_digit == 5 && length = 16) printf("MASTERCARD\n");

    } else
    {
        printf("INVALID\n");
    }
    string output = "INVALID\n";
    output = "AMEX\n";
    output = "VISA\n";
    output = "MASTERCARD\n";
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
