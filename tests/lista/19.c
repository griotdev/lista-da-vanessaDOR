#include <stdio.h>

void losango(int lines)
{
    int caracteres = 1;
    int maiorLinha = lines * 2 + 1;
    for (float i = 1; i <= lines; i++)
    {
        for (int k = 0; k < (maiorLinha / 2.0) - (caracteres / 2.0) + 1; k++)
        {
            printf(" ");
        }
        for (int j = 0; j < caracteres; j++)
        {
            printf("%%");
        }
        printf("\n");
        if (lines / i > 2.0)
        {
            caracteres += 4;
        }
        else if (lines / i < 2.0)
        {
            caracteres -= 4;
        }
    }
}

void triangulo(int lines)
{
    int maiorLinha = (lines * 2) - 1;
    int caracteres = 1;

    for (int i = 1; i <= lines; i++)
    {
        for (int j = 0; j < (maiorLinha - caracteres); j++)
        {
            printf(" ");
        }

        for (int k = 0; k < caracteres; k++)
        {
            printf("%%");
        }
        printf("\n");
        caracteres += 2;
    }
}

int main()
{
    int lines;
    int option;

    printf("\n\n=======================================\n");
    printf("   Bem vindo à ferramenta mais inútil\n");
    printf("   e elegante de toda a matéria...");
    printf("\n=======================================\n");

    printf("Escolha a opção:\n\n(1) Triângulo\n(2) Losango\n\n");
    scanf("%d", &option);

    printf("Insira a quantidade de linhas: ");
    scanf("%d", &lines);

    switch (option)
    {
    case 1:
        printf("\n");
        triangulo(lines);
        break;
    case 2:
        printf("\n");
        losango(lines);
        break;

    default:
        printf("Opção inválida.");
        break;
    }

    return 0;
}