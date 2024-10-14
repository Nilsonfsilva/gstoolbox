import os

def test_syntax_of_bash_scripts(host):
    # Encontra todos os arquivos no diretório src/ que possuem shebang para bash
    bash_scripts = host.run("grep -rl '^#!/usr/bin/env bash' src/").stdout.splitlines()

    for script in bash_scripts:
        # Verifica a sintaxe de cada script
        syntax_check = host.run(f"bash -n {script}")

        # Verifica se o código de saída foi 0 (sucesso)
        assert syntax_check.rc == 0, f"Erro de sintaxe encontrado no script {script}: {syntax_check.stdout} {syntax_check.stderr}"

        # Imprime mensagem de sucesso
        print(f"Syntax check passed for {script}")

