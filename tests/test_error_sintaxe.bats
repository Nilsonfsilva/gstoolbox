#!/usr/bin/env bats

# Define o caminho para o seu script
setup() {
    export SCRIPT_PATH="../src/create_repo"
}

@test "Check syntax of create_repo script with ShellCheck" {
    run shellcheck "$SCRIPT_PATH"
    [ "$status" -eq 0 ]
}
