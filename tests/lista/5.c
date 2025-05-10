#include <stdio.h>

int fatorial(int n)
{
    int fatorial = n;
    for (int i = n-1; i > 0; i--)
    {
        fatorial = fatorial * i;
    }
}

int main()
{

    int number;

    for (int i = 0; i < 7; i++)
    {
        printf("Insira o valor: ");
        scanf("%d", &number);

        printf("Fatorial: %d\n", fatorial(number));
    }

    return 0;
}