## Execução do projeto criado

Após criar o projeto, acesse o diretório `src` e execute o seguinte comando:

```bash
dotnet restore
```

Realize também o build do projeto, através do comando abaixo:

```bash
dotnet build
```

Para testar a aplicação, acesse o diretório que contém o projeto da api. O diretório é o `*.Api`. Dentro deste diretório, execute o seguinte comando:

```bash
dotnet run
```

Com a aplicação em execução, acesse a url https://localhost:5001/swagger, acesse os detalhes da aplicação e clique em "Ir para localhost (não seguro)". Ao acessar o endereço acima, você poderá ver a documentação de sua aplicação.

> Dica: Neste caso, a estrutura com exemplo foi criada automaticamente. 