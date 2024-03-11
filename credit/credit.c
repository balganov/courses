#include <cs50.h>
#include <stdio.h>

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

    printf("before loop %i\n",sum);

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

    string output = "INVALID\n";
    output = "AMEX\n";
    output = "VISA\n";
    output = "MASTERCARD\n";


}
