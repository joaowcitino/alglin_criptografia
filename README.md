
# Enigma 🧩

**Enigma** é uma biblioteca Python simples para realizar criptografia baseada em algoritmos de matriz, inspirada na máquina Enigma. Esta biblioteca inclui métodos para criptografia e descriptografia de mensagens usando técnicas matemáticas e um servidor Flask que você pode executar para testar suas mensagens cifradas.

## Recursos ✨
- **Criptografia e descriptografia** utilizando transformação de mensagens para one-hot encoding e aplicação de permutações.
- **Simulação da máquina Enigma**, com um processo de criptografia mais complexo que varia a cada iteração.
- **Servidor Flask** que permite enviar mensagens por requisições HTTP POST e obter a mensagem cifrada e decifrada.
- **Exemplo prático (Demo)** de como usar as funções de criptografia e descriptografia diretamente do terminal.

## Instalação ⚙️

Para instalar a biblioteca, siga os passos abaixo:

### 1. Baixe a bibliteca pelo pip 

Primeiro, baixe a nossa biblioteca pelo pip utilizando o seguinte comando:

```bash
pip install git+https://github.com/joaowcitino/alglin_criptografia.git
```

### 2. Execute a biblioteca

Agora, execute a biblioteca localmente usando o `python`:

```bash
enigma-server
```

Isso irá iniciar o nosso sistema junto com um servidor `flask`.

### 4. Teste a API 🚀

Com o servidor Flask rodando, você pode enviar uma mensagem para criptografar e decifrar. Por exemplo, utilizando `curl`:

```bash
curl -X POST http://127.0.0.1:5000/criptografia \
     -H "Content-Type: application/json" \
     -d '{"mensagem": "hello world"}'
```

A resposta será algo como:

```json
{
  "mensagem_cifrada": "xrllw uqrlp",
  "mensagem_decifrada": "hello world",
  "mensagem_cifrada_enigma": "xglli wqilr",
  "mensagem_decifrada_enigma": "hello world"
}
```

## Exemplo de Uso (Demo) 💻

Você também pode executar o script de demo diretamente pelo terminal para ver o funcionamento da criptografia e descriptografia sem o servidor Flask.

Execute o seguinte comando no diretório raiz do projeto, para isso deve clonar esse repositório:

```bash
python demo.py
```

O script solicitará uma mensagem para ser cifrada e, em seguida, exibirá a mensagem cifrada e decifrada usando diferentes técnicas.

## Como Funciona o Sistema ⚙️

### Estrutura do Projeto

```bash
enigma_library/
│
├── enigma/
│   ├── __init__.py  # Inicializa o pacote
│   ├── main.py      # Código principal do Flask e criptografia
│
├── demo.py          # Exemplo de uso da biblioteca
├── setup.py         # Arquivo de configuração para instalação
```

### Principais Funções de Criptografia

- **`cifrar(msg, P, alfabeto)`**: Função que criptografa a mensagem `msg` utilizando uma matriz de permutação `P` e o `alfabeto`.
- **`de_cifrar(msg, P, alfabeto)`**: Função que descriptografa a mensagem criptografada `msg` utilizando a matriz de permutação `P`.
- **`enigma(msg, P, E, alfabeto)`**: Simula a máquina Enigma, utilizando duas matrizes de permutação `P` e `E`, que variam a cada caractere da mensagem.
- **`de_enigma(msg, P, E, alfabeto)`**: Descriptografa uma mensagem cifrada com o algoritmo Enigma.

### Flask API

O servidor Flask fornece uma API simples com o seguinte endpoint:

- **POST `/criptografia`**: Envia uma mensagem JSON contendo a mensagem a ser cifrada. A resposta inclui a mensagem cifrada e decifrada, tanto com a técnica simples quanto com a técnica Enigma.

Exemplo de corpo da requisição:

```json
{
    "mensagem": "hello world"
}
```

### Exemplo de Configuração do `setup.py`

O arquivo `setup.py` está configurado para incluir um entry point que permite rodar o servidor Flask diretamente pelo terminal. O comando `enigma-server` executa o servidor Flask definido no arquivo `main.py`.

```python
entry_points={
    'console_scripts': [
        'enigma-server=enigma.main:app.run',  # Executa o servidor Flask
    ],
},
```

## Contribuindo 🛠️

Contribuições são bem-vindas! Siga os passos abaixo para contribuir com o projeto:

1. Faça um fork do repositório.
2. Crie um branch para suas alterações: `git checkout -b minha-feature`.
3. Envie suas alterações: `git commit -am 'Minha nova feature'`.
4. Envie o branch: `git push origin minha-feature`.
5. Crie um novo Pull Request.

## Contato 📬

Criado por **João Whitaker Citino** e **João Gabriel Delomo**. Se tiver alguma dúvida ou sugestão, entre em contato:

- Email: [joaocitino10@gmail.com](mailto:joaocitino10@gmail.com)
- Email: [joaogabriel.delomo@gmail.com](mailto:joaogabriel.delomo@gmail.com)
- GitHub: [github.com/joaowcitino](https://github.com/joaowcitino)
- GitHub: [github.com/JoaoDelomo](https://github.com/JoaoDelomo)

---

Feito com 💖 por João Citino e João Delomo.