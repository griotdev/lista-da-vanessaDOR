#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main()
{

    int number;

    while (true)
    {
        scanf("%d", &number);

        if (number <= 0)
        {
            break;
        }

        if (number % 2 == 0)
        {
            printf("%d\n", number * number);
        }
        else
        {
            printf("%.2f\n", sqrt(number));
        }
    }

    return 0;
}