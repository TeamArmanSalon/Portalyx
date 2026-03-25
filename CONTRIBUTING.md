# Contributing to Portalyx

Welcome to the Portalyx repository! This guide provides a beginner-friendly overview of Git and GitHub concepts for newcomers to help you contribute effectively.

## What is Git?
Git is a version control system that lets you manage and keep track of your source code history. It allows multiple people to work on a project without overwriting each other's changes.

## What is GitHub?
GitHub is a web-based platform that uses Git and provides a collaborative environment for software development. It allows you to host your repositories online, make contributions, track issues, and much more.

## Basic Concepts
- **Repository (Repo)**: A repository is a place where your project files are stored. GitHub hosts repositories online.
- **Commit**: A commit is a snapshot of your project at a certain point in time.
- **Branch**: A branch is a separate line of development. You can work on features without affecting the main codebase.
- **Merge**: Merging is combining changes from different branches.

## How to Get Started
1. **Create a GitHub Account**: Sign up at [GitHub](https://github.com).
2. **Install Git**: Download and install Git from [git-scm.com](https://git-scm.com).
3. **Clone the Repository**:
   Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/TeamArmanSalon/Portalyx.git
   ```
4. **Create a Branch**:
   Navigate to the cloned directory and create a new branch for your feature:
   ```bash
   cd Portalyx
   git checkout -b my-feature
   ```
5. **Make Changes**: Modify the files using your favorite code editor.
6. **Stage Your Changes**: Add the changes to your local repository:
   ```bash
   git add .
   ```
7. **Commit Your Changes**:
   Record your changes with a commit:
   ```bash
   git commit -m "Add my feature"
   ```
8. **Push Your Changes**: To upload your changes to GitHub:
   ```bash
   git push origin my-feature
   ```
9. **Create a Pull Request**: Go to the GitHub repository page, find your branch, and click on 'New Pull Request'. Provide a description and submit.

## Common Git Commands
- `git status`: Check the status of your working directory.
- `git log`: View your commit history.
- `git merge branch-name`: Merge a specified branch into the current branch.
- `git branch`: List all branches in your repository.

## Troubleshooting Tips
- If you encounter merge conflicts, Git will highlight the conflicting files. Open them and manually resolve the conflicts.
- Always pull the latest changes from the main branch before starting a new feature:
   ```bash
   git checkout main
   git pull origin main
   ```

## Conclusion
Contributing to an open-source project can be a valuable experience. Familiarize yourself with Git and GitHub to enhance your development skills. Happy coding!