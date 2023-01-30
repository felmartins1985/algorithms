# Algoritmos 🧩💻 

Consiste em seis desafios propostos pela [Trybe]() para resolução e otimização dos algoritmos, aplicando os conceitos de recursividade e iteratividade; complexidade de tempo e espaço; aplicação de algoritmos de busca e ordenação não nativos do Python e realizações de testes.

* Solucionado com a utilizando da linguagem Python

<br />

<details>
  <summary><strong>Descrição das soluções criadas:</strong></summary><br />

| Função | Descrição | Localização |
|---|---|---|
| `study_schedule` | Retorna o número de estudantes online mediante os horários informados no array de tuplas em comparação com a hora informada | `challenges/challenge_study_schedule.py` |
| `is_palindrome_recursive` | Avaliar se uma palavra é palíndroma, de forma recursiva | `challenges/challenge_palindromes_recursive.py` |
| `is_anagram` | Avaliar se as palavras informada são anagramas | `challenges/challenge_anagrams.py` |
| `find_duplicate` | Dentro de um array de números, retorna o número duplicado | `challenge_find_the_duplicate.py` |
| `is_palindrome_iterative` | Avaliar se uma palavra é palíndroma, de forma iteratividade | `challenge_palindromes_iterative.py` |


<br />
</details>

<details>
  <summary><strong>Descrição do teste criado:</strong></summary><br />
 
| Teste | Descrição | Localização |
|---|---|---|
| `test_encrypt_message` | Criação dos testes para função de criptografia de palavras | `tests/encrypt/test_encrypt.py` |


<br />
</details>

### Estrutura do Projeto

```
.
├── challenges
│   ├──🔹 challenge_anagrams.py
│   ├──🔸 challenge_encrypt_message.py
│   ├──🔹 challenge_find_the_duplicate.py
│   ├──🔹 challenge_palindromes_iterative.py
│   ├──🔹 challenge_palindromes_recursive.py
│   └──🔹 challenge_study_schedule.py
├── tests
│   ├── encrypt
│   │   ├──🔸 __init__.py
│   │   └──🔹 test_encrypt.py
│   ├──🔸 __init__.py
│   ├──🔸 complexities.py
│   └──🔸 geradores.py
├──🔸 dev-requirements.txt
├──🔸 pyproject.toml
├──🔸 README.md
├──🔸 requirements.txt
├──🔸 setup.cfg
└──🔸 setup.py

Legenda:
🔸 Arquivos desenvolvidos pela Trybe (não foram alterados).
🔹 Arquivos desenvolvidos por mim.

```



### Instruções

- Realize o clone do projeto e utilize os comandos a seguir:

```
Para instalar as dependências e iniciar as aplicações:
<-- na raiz do projeto -->
python3 -m venv .venv // para criar o ambiente virtual
source .venv/bin/activate // para ativar o ambiente virtual
python3 -m pip install -r dev-requirements.txt // instalação das dependências


Para rodar os testes:
<-- na raiz do projeto -->
python3 -m pytest
```
