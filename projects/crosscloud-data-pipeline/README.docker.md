Use this Docker-based verification (use if local pip builds fail on Windows)
---------------------------------------------------------------

### Why
Windows can be picky about compiling Python packages. If a local install gives you trouble, run the project inside the provided Docker image so you know you're starting from a clean Linux environment.

### Quick local test (requires Docker Desktop)
```bash
cd projects/crosscloud-data-pipeline
docker build -t crosscloud-pipeline:local .
docker run --rm crosscloud-pipeline:local python src/generator.py
```

This mirrors what GitHub Actions does and proves the project builds cleanly in a vanilla container.

