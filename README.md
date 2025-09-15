# Calculadora de Combustível

Um aplicativo multiplataforma desenvolvido com Kivy/Python para ajudar motoristas a decidir entre abastecer com gasolina ou etanol, calcular o consumo médio do veículo e estimar gastos com combustível em viagens.

## Funcionalidades

- **Calculadora de Combustível**: Compara os preços de gasolina e etanol e indica qual é mais vantajoso (usando a regra dos 70%).
- **Cálculo de Consumo Médio**: Calcula o consumo médio do veículo em km/L.
- **Estimativa de Gastos**: Estima o gasto com combustível para uma determinada distância.
- **Interface amigável**: Design moderno e intuitivo.
- **Multiplataforma**: Funciona em Android, iOS, Windows, macOS e Linux.

## Requisitos

- Python 3.7 ou superior
- Kivy 2.1.0 ou superior

## Instalação

### Instalação do Python

Se você ainda não tem o Python instalado, baixe e instale a versão mais recente em [python.org](https://www.python.org/downloads/).

### Instalação do Kivy

```bash
pip install kivy
```

Ou, para uma instalação mais completa com todas as dependências:

```bash
pip install kivy[base,media,tuio]
```

### Clonando o repositório

```bash
git clone https://github.com/dreduardocruz/combustivel.git
cd combustivel
```

## Executando o aplicativo

### No computador (Windows, macOS, Linux)

```bash
python main.py
```

### Empacotando para Android

Para empacotar o aplicativo para Android, você precisará do Buildozer:

```bash
pip install buildozer
```

Crie um arquivo buildozer.spec:

```bash
buildozer init
```

Edite o arquivo buildozer.spec conforme necessário e execute:

```bash
buildozer -v android debug
```

### Empacotando para iOS

Para empacotar para iOS, você precisará de um Mac com Xcode instalado e o toolchain do Kivy-iOS:

```bash
pip install kivy-ios
toolchain build kivy
toolchain create calculadora-combustivel /caminho/para/seu/app
```

## Uso

1. Na tela inicial, insira os preços da gasolina e do etanol para calcular qual combustível é mais vantajoso.
2. Navegue para a tela de Consumo Médio para calcular o consumo do seu veículo.
3. Use a tela de Estimativa de Gastos para planejar seus gastos com combustível em viagens.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
