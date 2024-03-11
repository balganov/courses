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

    int sum = (card_number % 10)*2;
    printf("before loop %i\n",sum);

    for (long i = 100; i < 100000000000000; i=i*100)
    {
        sum = sum + (card_number/i % 10)*2;
        printf("%li in the loop %i\n",i,sum);
    }

    printf("afer the loop %i\n",sum);

    string output = "INVALID\n";
    output = "AMEX\n";
    output = "VISA\n";
    output = "MASTERCARD\n";


}
