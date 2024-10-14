import subprocess
from unittest.mock import mock_open, patch
import os

SCRIPT_PATH = 'src/select_del'

def test_select_repo(mocker):
    # Simulando a leitura do arquivo
    mocker.patch("builtins.open", mock_open(read_data="1 repo1\n2 repo2\n"))
    
    # Simulando a variável de ambiente necessária para o script
    mocker.patch.dict(os.environ, {"GITLAB_TOKEN": "valid_token"})

    with patch("builtins.print") as mocked_print:
        with patch("builtins.input", return_value='1'):
            result = subprocess.run([SCRIPT_PATH], capture_output=True, text=True)

            # Imprimindo informações de depuração
            print(f"Return Code: {result.returncode}")
            print(f"Output: {result.stdout}")
            print(f"Error: {result.stderr}")

            # Verifica se o script foi executado com sucesso
            assert result.returncode == 0
