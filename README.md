# Lista da Wanessador

Uma aplicação Python simples que gera um PDF contendo todos os arquivos de código fonte em C encontrados em um diretório específico.

## Funcionalidades

- Escaneia recursivamente um diretório em busca de arquivos fonte em C
- Cria um PDF com todo o código C encontrado, um exercício por página
- Ordenação natural dos arquivos (1, 2, 3, ..., 10, 11 em vez de 1, 10, 11, ...)
- Suporte para argumentos de linha de comando e modo interativo

## Instalação

1. Clone este repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

### Modo Interativo

```bash
./run.py
```

Você será solicitado a inserir:

- O caminho para o diretório contendo os arquivos C
- O nome do arquivo PDF de saída

### Modo de Linha de Comando

```bash
./run.py -d /caminho/para/arquivos/c -o saida.pdf
```

Argumentos:

- `-d, --directory`: Caminho para o diretório contendo os arquivos fonte em C
- `-o, --output`: Nome do arquivo PDF de saída

Você também pode fornecer apenas um dos argumentos:

```bash
./run.py -d /caminho/para/arquivos/c
```

Neste caso, você será solicitado a inserir apenas o nome do arquivo de saída.

```bash
./run.py -o saida.pdf
```

Neste caso, você será solicitado a inserir apenas o caminho do diretório.

## Estrutura do Projeto

```
.
├── README.md
├── requirements.txt
├── run.py
└── src/
    ├── __init__.py
    ├── main.py
    ├── cli.py
    ├── pdf_generator.py
    └── utils.py
```

## Licença

Este projeto é de código aberto e disponível sob a Licença MIT.

## Contribuindo

Contribuições, problemas e solicitações de recursos são bem-vindos!
