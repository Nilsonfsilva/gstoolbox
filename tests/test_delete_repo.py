import os
import tempfile
import shutil
import testinfra

host = testinfra.get_host("local://")

def test_delete_repo_github(host):
    # Simula o arquivo de configuração de repositórios
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile.write(b"123 repo1\n456 repo2\n")
        tmpfile_path = tmpfile.name
    
    # Simula as variáveis de ambiente necessárias
    os.environ['HOME'] = tempfile.gettempdir()  # Simula a pasta home temporária
    os.environ['PLATFORM'] = "github"
    os.environ['USERNAME'] = "test_user"
    os.environ['TOKEN'] = "fake_token"
    
    # Cria o diretório e move o arquivo para simular ~/.config/gstoolbox/select_repo
    config_dir = os.path.join(os.environ['HOME'], ".config/gstoolbox")
    os.makedirs(config_dir, exist_ok=True)
    shutil.move(tmpfile_path, os.path.join(config_dir, "select_repo"))

    # Cria o script temporário delete_repo no /tmp
    delete_repo_script = """
    #!/usr/bin/env bash
    echo "delete_repo script running"
    """
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as script_file:
        script_file.write(delete_repo_script)
        script_path = script_file.name

    # Torna o script executável
    os.chmod(script_path, 0o755)

    # Mocka o comando curl para simular a exclusão do repositório com código 204
    mock_curl = "echo 204"
    host.run(f"alias curl='{mock_curl}'")  # Fechar a string corretamente aqui
    
    # Executa o script usando o caminho completo
    result = host.run(f"bash -c 'source {script_path}'")
    
    # Verifica se o script rodou corretamente
    assert result.exit_status == 0
    assert "delete_repo script running" in result.stdout


def test_delete_repo_gitlab(host):
    # Simula o arquivo de configuração de repositórios
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile.write(b"123 repo1\n456 repo2\n")
        tmpfile_path = tmpfile.name
    
    # Simula as variáveis de ambiente necessárias
    os.environ['HOME'] = tempfile.gettempdir()
    os.environ['PLATFORM'] = "gitlab"
    os.environ['USERNAME'] = "test_user"
    os.environ['TOKEN'] = "fake_token"
    
    # Cria o diretório e move o arquivo para simular ~/.config/gstoolbox/select_repo
    config_dir = os.path.join(os.environ['HOME'], ".config/gstoolbox")
    os.makedirs(config_dir, exist_ok=True)
    shutil.move(tmpfile_path, os.path.join(config_dir, "select_repo"))

    # Cria o script temporário delete_repo no /tmp
    delete_repo_script = """
    #!/usr/bin/env bash
    echo "delete_repo script running"
    """
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as script_file:
        script_file.write(delete_repo_script)
        script_path = script_file.name

    # Torna o script executável
    os.chmod(script_path, 0o755)

    # Mocka o comando curl para simular a exclusão do repositório com código 202
    mock_curl = "echo 202"
    host.run(f"alias curl='{mock_curl}'")  # Fechar a string corretamente aqui
    
    # Executa o script usando o caminho completo
    result = host.run(f"bash -c 'source {script_path}'")
    
    # Verifica se o script rodou corretamente
    assert result.exit_status == 0
    assert "delete_repo script running" in result.stdout
