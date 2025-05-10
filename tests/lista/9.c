#include <stdio.h>

int main() {

    int maior;
    int menor;
    int numeroAtual;

    for (int i = 0;  i < 30; i++) {
        printf("Insira o número:");
        scanf("%d", &numeroAtual);
        if (i == 0) {
            maior = numeroAtual;
            menor = numeroAtual;
        } else if (numeroAtual > maior) {
            maior = numeroAtual;
        } else if (numeroAtual < menor) {
            menor = numeroAtual;
        }
    }

    printf("Número maior: %d\n", maior);
    printf("Número menor: %d\n", menor);

    return 0;
}