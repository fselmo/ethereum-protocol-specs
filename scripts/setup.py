#!/usr/bin/env python3
"""Initial setup script for the Ethereum Protocol Specs template."""

import os
import re
import sys
from pathlib import Path
from typing import Dict


def get_user_input() -> Dict[str, str]:
    """Collect project information from the user."""
    print("\n🚀 Welcome to the Ethereum Protocol Specs Template Setup!\n")
    
    config = {}
    
    # Project name
    default_project_name = Path.cwd().name
    config['project_name'] = input(
        f"Project name [{default_project_name}]: "
    ).strip() or default_project_name
    
    # Package name (sanitized version)
    default_package_name = re.sub(r'[^a-zA-Z0-9_-]', '-', config['project_name'].lower())
    config['package_name'] = input(
        f"Package name [{default_package_name}]: "
    ).strip() or default_package_name
    
    # GitHub organization/user
    config['github_org'] = input(
        "GitHub organization or username [ethereum]: "
    ).strip() or "ethereum"
    
    # Author name
    config['author_name'] = input(
        "Author name [Ethereum Foundation]: "
    ).strip() or "Ethereum Foundation"
    
    # Author email
    config['author_email'] = input(
        "Author email [security@ethereum.org]: "
    ).strip() or "security@ethereum.org"
    
    # Year for copyright
    from datetime import datetime
    current_year = datetime.now().year
    config['year'] = input(
        f"Copyright year [{current_year}]: "
    ).strip() or str(current_year)
    
    return config


def replace_in_file(file_path: Path, replacements: Dict[str, str]) -> None:
    """Replace placeholders in a single file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        file_path.write_text(content, encoding='utf-8')
        print(f"✓ Updated: {file_path}")
    except Exception as e:
        print(f"✗ Error updating {file_path}: {e}")


def setup_project(config: Dict[str, str]) -> None:
    """Replace all placeholders in the project."""
    # Define replacements
    replacements = {
        '{PROJECT_NAME}': config['project_name'],
        '{PACKAGE_NAME}': config['package_name'],
        '{GITHUB_ORG}': config['github_org'],
        '{AUTHOR_NAME}': config['author_name'],
        '{AUTHOR_EMAIL}': config['author_email'],
        '{YEAR}': config['year'],
        
        # Also replace current values for repos cloned directly
        'ethereum-protocol-specs': config['package_name'],
        'ethereum-specs': config['package_name'],
        'Your Name': config['author_name'],
        'your.email@example.com': config['author_email'],
        'Ethereum Foundation': config['author_name'],
        '2025': config['year'],
        '2024': config['year'],
        'ethereum/ethereum-protocol-specs': f"{config['github_org']}/{config['package_name']}",
        'https://github.com/ethereum/...': f"https://github.com/{config['github_org']}/{config['package_name']}",
    }
    
    # Files to update
    files_to_update = [
        'pyproject.toml',
        'mkdocs.yml',
        'README.md',
        'LICENSE',
        'docs/index.md',
        '.github/ISSUE_TEMPLATE/bug_report.md',
        '.github/ISSUE_TEMPLATE/feature_request.md',
    ]
    
    # Process each file
    root = Path.cwd()
    for file_path in files_to_update:
        full_path = root / file_path
        if full_path.exists():
            replace_in_file(full_path, replacements)
        else:
            print(f"⚠ File not found: {file_path}")
    
    # Update <repository-url> placeholders
    for file_path in ['README.md', 'docs/index.md']:
        full_path = root / file_path
        if full_path.exists():
            content = full_path.read_text(encoding='utf-8')
            content = content.replace(
                '<repository-url>',
                f'https://github.com/{config["github_org"]}/{config["package_name"]}'
            )
            full_path.write_text(content, encoding='utf-8')
    
    print("\n✅ Setup complete!")
    print(f"\nYour project '{config['project_name']}' is ready!")
    print("\nNext steps:")
    print("1. Delete the setup script: rm scripts/setup.py")
    print("2. Update the uv.lock: uv sync")
    print("3. Run tests: uv run pytest")
    print("4. Start developing your Ethereum specifications! 🎉")


def main():
    """Main entry point."""
    # Check if we're in the right directory
    if not Path('pyproject.toml').exists():
        print("❌ Error: pyproject.toml not found.")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check if this is still a template (has placeholders)
    pyproject_content = Path('pyproject.toml').read_text()
    if '{PACKAGE_NAME}' not in pyproject_content:
        print("❌ Error: This project has already been configured.")
        print("The setup script should only be run on a fresh template.")
        sys.exit(1)
    
    try:
        config = get_user_input()
        
        print("\n📋 Configuration Summary:")
        print(f"  Project Name: {config['project_name']}")
        print(f"  Package Name: {config['package_name']}")
        print(f"  GitHub: {config['github_org']}/{config['package_name']}")
        print(f"  Author: {config['author_name']} <{config['author_email']}>")
        print(f"  Copyright Year: {config['year']}")
        
        confirm = input("\nProceed with setup? [Y/n]: ").strip().lower()
        if confirm in ['', 'y', 'yes']:
            setup_project(config)
        else:
            print("Setup cancelled.")
    except KeyboardInterrupt:
        print("\n\nSetup cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()