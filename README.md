
# 🛠️ Git Shell Toolbox (gstoolbox)

**Git Shell Toolbox (gstoolbox)** é uma poderosa ferramenta de linha de comando (CLI) que facilita e automatiza tarefas comuns no gerenciamento de repositórios Git, suportando **GitHub**, **GitLab** e **Salsa**. Com gstoolbox, você pode **excluir, criar, listar arquivos, buscar repositórios, clonar e enviar projetos** - tudo sem precisar navegar pela interface web. Utilize APIs e tokens de autenticação para um processo rápido, seguro e eficiente.

## 🚀 Funcionalidades

- **🔗 Suporte para múltiplas plataformas:** Gerencie repositórios no GitHub, GitLab e Salsa de forma integrada.
- **🗑️ Excluir um ou múltiplos repositórios:** Simplifique a gestão de repositórios, excluindo vários de uma só vez ou apenas um.
- **📁 Criar novos repositórios:** Crie repositórios rapidamente em qualquer uma das plataformas suportadas.
- **📋 Listar arquivos em repositórios:** Obtenha uma visão geral dos arquivos contidos em seus repositórios.
- **🔍 Buscar repositórios:** Encontre rapidamente repositórios por nome ou critérios específicos.
- **📂 Clonar repositórios:** Clone repositórios diretamente para seu ambiente de trabalho.
- **📤 Enviar projetos:** Envie mudanças e atualizações para os repositórios diretamente via CLI.
- **🔐 Gerenciamento seguro de tokens:** Gerencie seus tokens de API de forma segura, garantindo suporte a diversas plataformas.
- **💻 Integração com o terminal:** Ideal para usuários que preferem a agilidade e eficiência do terminal.

## 📦 Instalação

1. **Clone o repositório gstoolbox:**
    ```bash
    git clone https://github.com/usuario/gstoolbox.git
    ```

2. **Navegue até o diretório gstoolbox:**
    ```bash
    cd gstoolbox
    ```

3. **Instale as dependências (se houver):**
    ```bash
    # Exemplo de comando, caso seja necessário instalar dependências
    pip install -r requirements.txt
    ```

4. **Configure seu token de API:**
    ```bash
    export GIT_API_TOKEN=seu_token_aqui
    ```

## 🛠️ Uso

Aqui estão alguns dos comandos principais que você pode utilizar com o gstoolbox:

- **🗑️ Excluir repositórios:**
    ```bash
    gstoolbox --delete plataforma usuário token
    ```
    Exclua um ou múltiplos repositórios de uma só vez.

- **📁 Criar um novo repositório:**
    ```bash
    gstoolbox --create plataforma usuário token
    ```

- **📋 Listar arquivos de um repositório:**
    ```bash
    gstoolbox list-files nome_do_repo
    ```

- **🔍 Buscar repositórios:**
    ```bash
    gstoolbox --find plataforma usuário token
    ```

- **📂 Clonar um repositório:**
    ```bash
    gstoolbox clone-repo nome_do_repo
    ```

- **📤 Enviar mudanças para um repositório:**
    ```bash
    gstoolbox push-repo nome_do_repo
    ```

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📝 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## 🙏 Agradecimentos

Agradecemos a todos os contribuidores e à comunidade de código aberto por seu apoio e colaboração.
