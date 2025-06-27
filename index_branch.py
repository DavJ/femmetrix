from git import Repo
import os
import json
from elasticsearch import Elasticsearch
from datetime import datetime

REPO_PATH = "/path/to/femmetrix"
BRANCH = "main"

es = Elasticsearch("http://localhost:9200")
INDEX = "femmetrix-code"

repo = Repo(REPO_PATH)
repo.git.checkout(BRANCH)

for root, dirs, files in os.walk(REPO_PATH):
    for file in files:
        if file.endswith(('.py', '.yaml', '.js', '.tsx')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            rel_path = os.path.relpath(filepath, REPO_PATH)
            doc = {
                "repo": "femmetrix",
                "branch": BRANCH,
                "commit": repo.head.commit.hexsha[:8],
                "filepath": rel_path,
                "filename": file,
                "filetype": file.split(".")[-1],
                "content": content,
                "indexed_at": datetime.utcnow().isoformat()
            }
            es.index(index=INDEX, body=doc)
