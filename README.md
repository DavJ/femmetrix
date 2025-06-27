# AI Agents Core for Any Project

This folder contains reusable AI agents and scripts to support development and testing automation.

## Included

- `elastic_indexer.yaml`: Agent to index code files per branch into Elasticsearch.
- `index_branch.py`: Script to scan a git branch and index files into Elasticsearch.

## Usage

1. Adjust `REPO_PATH` and `BRANCH` in `index_branch.py`.
2. Run the script to populate the `femmetrix-code` index.
3. Agents can query Elasticsearch to retrieve code context.
