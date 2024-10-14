def test_create_repo_script(host):
    # Simula as entradas necessárias escolhendo uma plataforma e omitindo o token
    cmd = host.run("printf '1\nuser\nrepo\n1\n\n' | bash src/create_repo")

    # Verifica a saída completa
    print("STDOUT:", cmd.stdout)
    print("STDERR:", cmd.stderr)

    # Verifica se o código de saída não foi 0 (esperamos erro)
    assert cmd.rc != 0, f"Esperava erro, mas obteve sucesso: {cmd.rc}: {cmd.stdout} {cmd.stderr}"

    # Verifica se a mensagem "Bad credentials" ou similar está presente
    assert "Bad credentials" in cmd.stdout or "Failed to create repository" in cmd.stdout, \
        "A mensagem de erro esperada não foi encontrada."
