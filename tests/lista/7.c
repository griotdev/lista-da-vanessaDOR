#include <stdio.h>

int main()
{
    int lines;

    printf("Insira a quantidade de linhas: ");
    scanf("%d", &lines);

    int sum = 1;
    for (int i = 0; i < lines; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            printf("%d\t", sum);
            sum += 1;
        }
        printf("\n");
    }

    return 0;
}