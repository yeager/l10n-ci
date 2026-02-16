#!/bin/bash
set -e

# L10n CI/CD sync script
# Synchronizes translation files with Transifex

TX_TOKEN=${TX_TOKEN:-}
SOURCE_FILE=${SOURCE_FILE:-"po/*.pot"}
MIN_PERCENTAGE=${MIN_PERCENTAGE:-10}
COMMIT_MESSAGE=${COMMIT_MESSAGE:-"i18n: sync translations from Transifex"}

if [ -z "$TX_TOKEN" ]; then
    echo "Error: TX_TOKEN environment variable is required"
    exit 1
fi

echo "Installing Transifex CLI..."
curl -o- https://raw.githubusercontent.com/transifex/cli/master/install.sh | bash
sudo mv tx /usr/local/bin/

echo "Pushing source files to Transifex..."
tx push -s --skip

echo "Pulling translations from Transifex (minimum ${MIN_PERCENTAGE}%)..."
tx pull -a --force --minimum-perc "$MIN_PERCENTAGE"

echo "Committing changes..."
git config user.name "L10n CI/CD"
git config user.email "noreply@github.com"
git add po/*.po

if ! git diff --cached --quiet; then
    git commit -m "$COMMIT_MESSAGE"
    git push
    echo "Translation updates committed and pushed."
else
    echo "No translation changes to commit."
fi