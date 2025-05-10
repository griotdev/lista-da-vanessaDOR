#include <stdio.h>

int main()
{

    int number;
    int divisores;
    int somatorio;

    for (int i = 0; i < 10; i++)
    {
        somatorio = 0;
        divisores = 0;
        printf("Insira o número: ");
        scanf("%d", &number);

        for (int i = 1; i <= number; i++)
        {
            somatorio += i;
        }
        printf("Somatório de %d: %d\n", number, somatorio);

        for (int i = number; i > 0; i--)
        {
            number % i == 0 ? divisores++ : 0;
        }
        printf("Divisores de %d: %d\n", number, divisores);
    }

    return 0;
}