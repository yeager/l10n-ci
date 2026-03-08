# l10n ci [![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/yeager/l10n-ci)



## Description

l10n ci is a GTK4/Adwaita application 

[Application description will be added based on individual repo functionality]

## Features

- Modern GTK4/Adwaita interface
- [Feature list to be customized per repo]



## Installation

### APT Repository (Debian/Ubuntu)

```bash
echo "deb https://yeager.github.io/debian-repo stable main" | sudo tee /etc/apt/sources.list.d/yeager-l10n.list
sudo apt update
sudo apt install l10n-ci
```

### DNF Repository (Fedora/RHEL)

```bash
sudo dnf config-manager --add-repo https://yeager.github.io/rpm-repo/yeager-l10n.repo
sudo dnf install l10n-ci
```

### Building from Source

```bash
git clone https://github.com/yeager/l10n-ci.git
cd l10n-ci
pip install -e .
```

## Translation

This application is managed on Transifex: https://app.transifex.com/danielnylander/l10n-ci/

Available in 11 languages: Swedish, German, French, Spanish, Italian, Portuguese, Dutch, Polish, Czech, Russian, and Chinese (Simplified).

## License

GPL-3.0-or-later

## Author

Daniel Nylander (daniel@danielnylander.se)
