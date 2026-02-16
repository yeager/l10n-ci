#!/usr/bin/env python3
"""
L10n CI/CD - GitHub Action for localization CI/CD workflows
"""

import sys
import subprocess
import os
import argparse

def run_sync(transifex_token, source_file="po/*.pot", min_percentage=10, commit_message="i18n: sync translations from Transifex"):
    """Run translation synchronization"""
    
    # Set environment variables
    env = os.environ.copy()
    env['TX_TOKEN'] = transifex_token
    env['SOURCE_FILE'] = source_file
    env['MIN_PERCENTAGE'] = str(min_percentage)
    env['COMMIT_MESSAGE'] = commit_message
    
    # Run sync script
    script_path = os.path.join(os.path.dirname(__file__), '..', '..', 'scripts', 'sync.sh')
    try:
        subprocess.run(['bash', script_path], env=env, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Sync failed with error: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="L10n CI/CD synchronization tool")
    parser.add_argument('--token', required=True, help='Transifex API token')
    parser.add_argument('--source-file', default='po/*.pot', help='Source file pattern')
    parser.add_argument('--min-percentage', type=int, default=10, help='Minimum translation percentage')
    parser.add_argument('--commit-message', default='i18n: sync translations from Transifex', help='Commit message')
    
    args = parser.parse_args()
    
    success = run_sync(
        transifex_token=args.token,
        source_file=args.source_file,
        min_percentage=args.min_percentage,
        commit_message=args.commit_message
    )
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()