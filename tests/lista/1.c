#include <stdio.h>

int main()
{

    int sum;
    for (int i = 1; i <= 10; i++)
    {

        int value;
        printf("Insira o %dº valor: ", i);
        scanf("%d", &value);
        sum += value;
    }

    float media = sum / 10.0;

    printf("A média é %2.f", media);

    return 0;
}