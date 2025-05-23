# GitHub Actions Workflow Documentation

## Build and Release Workflow

Este workflow automatiza o processo de build e release do projeto Lista da Vanessador para múltiplas plataformas.

### Quando é executado

- **Push para main**: Executa build e cria release automaticamente
- **Pull Request**: Executa apenas o build para validação

### Plataformas suportadas

- **Linux** (Ubuntu Latest)
- **Windows** (Windows Latest)  
- **macOS** (macOS Latest)

### O que faz

1. **Build Job**: 
   - Executa em paralelo nas 3 plataformas
   - Instala Python 3.11 e dependências
   - Executa PyInstaller para criar executáveis
   - Faz upload dos artefatos

2. **Release Job** (apenas em push para main):
   - Baixa todos os artefatos
   - Cria uma nova release com tag automática
   - Anexa os executáveis à release

### Estrutura dos artefatos

```
artifacts/
├── lista-da-vanessador-linux/
│   └── lista-da-vanessador-linux
├── lista-da-vanessador-windows/
│   └── lista-da-vanessador-windows.exe
└── lista-da-vanessador-macos/
    └── lista-da-vanessador-macos
```

### Tags de release

As releases são criadas automaticamente com o formato:
`v{YYYYMMDD}-{run_number}`

Exemplo: `v20241215-123`

### Permissões necessárias

O workflow utiliza `GITHUB_TOKEN` que é fornecido automaticamente pelo GitHub Actions com as permissões necessárias para:
- Criar releases
- Fazer upload de assets
- Ler o repositório

### Configuração adicional

Não é necessária nenhuma configuração adicional. O workflow está pronto para uso assim que for commitado para a branch main.

### Troubleshooting

1. **Build falha**: Verifique se todas as dependências estão no `requirements.txt`
2. **Release não é criada**: Certifique-se que o push foi feito diretamente na branch main
3. **Executável não funciona**: Verifique se não há dependências externas não incluídas no PyInstaller