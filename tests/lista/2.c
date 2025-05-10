#include <stdio.h>

int main()
{

    int pares[10];
    int impares[10];

    for (int i = 0; i < 10; i++)
    {
        int number;
        printf("Insira o número: ");
        scanf("%d", &number);

        if (number % 2 == 0)
        {
            pares[i] = number;
        }
        else
        {
            impares[i] = number;
        }
    }

    int valoresPares = 0;
    int somaImpares = 0;

    for (int i = 0; i < 10; i++)
    {
        if (pares[i] != 0)
        {
            valoresPares++;
        }
        somaImpares += impares[i];
    }

    printf("%d valoeres pares.", valoresPares);
    printf("A média dos ímpares é %.2f", (somaImpares / 10.0));

    return 0;
}