import os
import re
import testinfra.utils.ansible_runner

host = testinfra.get_host("local://")

def remove_ansi_sequences(text):
    # Remove sequências de cores ANSI
    return re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', text)

def test_error_select_repository(host):
    # Simula as variáveis de ambiente necessárias
    os.environ['PLATFORM'] = "GitHub"
    os.environ['USERNAME'] = "test_user"

    # Executa a função desejada dentro do script e captura a saída
    script_output = host.run("bash -c 'source src/default_message && error_select_repository'")

    # Remove as sequências ANSI da saída
    clean_output = remove_ansi_sequences(script_output.stdout)

    # Verifica a saída esperada
    expected_output = "Error selecting repository test_user on platform GitHub"
    assert expected_output in clean_output, f"Mensagem esperada não encontrada. Saída: {clean_output}"
