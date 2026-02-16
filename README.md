# L10n CI/CD

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Transifex](https://img.shields.io/badge/Transifex-translate-green.svg)](https://www.transifex.com/danielnylander/l10n-ci/)

GitHub Action for localization CI/CD workflows - automates translation synchronization with Transifex.

## Features

- Automated source file pushing to Transifex
- Translation pulling with configurable minimum percentage
- Git commit and push of updated translations
- Flexible configuration via inputs
- Command-line tool for local usage

## Usage as GitHub Action

Add this to your workflow file (e.g., `.github/workflows/l10n.yml`):

```yaml
name: Localization CI/CD
on:
  push:
    branches: [main]
    paths: ['po/*.pot']
  workflow_dispatch:

jobs:
  sync-translations:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: yeager/l10n-ci@v1
        with:
          transifex-token: ${{ secrets.TX_TOKEN }}
          source-file: 'po/*.pot'
          minimum-percentage: 10
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `transifex-token` | Transifex API token | Yes | - |
| `source-file` | Path to source translation file | No | `po/*.pot` |
| `minimum-percentage` | Minimum translation percentage to pull | No | `10` |
| `commit-message` | Commit message for translation updates | No | `i18n: sync translations from Transifex` |

## Usage as CLI Tool

Install and run locally:

```bash
pip install l10n-ci
l10n-ci --token YOUR_TX_TOKEN --min-percentage 50
```

## Setup

1. Create a Transifex API token
2. Add it as a repository secret named `TX_TOKEN`
3. Configure your `.tx/config` file
4. Add the workflow to your repository

## Translation

Help translate this action on [Transifex](https://www.transifex.com/danielnylander/l10n-ci/).

## Author

**Daniel Nylander**
- Email: daniel@danielnylander.se
- GitHub: [@yeager](https://github.com/yeager)

## License

This project is licensed under the GPL-3.0-or-later License - see the [LICENSE](LICENSE) file for details.