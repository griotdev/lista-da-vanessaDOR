#include <stdio.h>

int main()
{
    int repeticoes;
    printf("Insira a quantidade de repetições:");
    scanf("%d", &repeticoes);

    int maiorNumero = 0;
    int vezesEmQueApareceu = 0;

    for (int i = 0; i < repeticoes; i++)
    {
        int numeroAtual;
        printf("Insira o número: ");
        scanf("%d", &numeroAtual);

        if (numeroAtual > maiorNumero)
        {
            maiorNumero = numeroAtual;
            vezesEmQueApareceu = 1;
        }
        else if (numeroAtual == maiorNumero)
        {
            vezesEmQueApareceu++;
        }
    }
    return 0;
}