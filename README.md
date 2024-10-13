
# 🛠️ Git Shell Toolbox (gstoolbox)

**Git Shell Toolbox (gstoolbox)** is a powerful command-line tool (CLI) that facilitates and automates common tasks in Git repository management, supporting **GitHub**, **GitLab**, and **Salsa** platforms.

## 🚀 Features

- **🔗 Multi-platform support:** Manage repositories on GitHub, GitLab, and Salsa seamlessly.
- **🗑️ Delete one or multiple repositories:** Simplify repository management by deleting multiple repositories at once or just one.
- **📁 Create new repositories:** Quickly create repositories on any supported platform.
- **📋 List files in repositories:** Get an overview of the files in your repositories.
- **🔍 Search repositories:** Quickly find repositories by name or specific criteria.
- **📂 Clone repositories:** Clone repositories directly into your workspace.
- **📤 Push projects:** Push changes and updates to repositories directly via CLI.
- **🔐 Secure token management:** Manage your API tokens securely, supporting multiple platforms.
- **💻 Terminal integration:** Ideal for users who prefer the speed and efficiency of the terminal.

## 📦 Installation

1. **Clone the gstoolbox repository:**
    ```bash
    git clone https://github.com/user/gstoolbox.git
    ```

2. **Navigate to the gstoolbox directory:**
    ```bash
    cd gstoolbox
    ```

3. **Install the dependencies (if any):**
    ```bash
    # Example command, if you need to install dependencies
    pip install -r requirements.txt
    ```

4. **Set up your API token:**
    ```bash
    export GIT_API_TOKEN=your_token_here
    ```

## 🛠️ Usage

Here are some of the main commands you can use with gstoolbox:

- **🗑️ Delete repositories:**
    ```bash
    gstoolbox --delete platform user token
    ```
    Delete one or multiple repositories at once.

- **📁 Create a new repository:**
    ```bash
    gstoolbox --create platform user token
    ```

- **📋 List repository files:**
    ```bash
    gstoolbox list-files repo_name
    ```

- **🔍 Search repositories:**
    ```bash
    gstoolbox --find platform user token
    ```

- **📂 Clone a repository:**
    ```bash
    gstoolbox clone-repo repo_name
    ```

- **📤 Push changes to a repository:**

^G Help         ^O Save        ^W Where Is?    ^

## 🤝 Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgments

Special thanks to all contributors and the open-source community for their support and collaboration.
