Docker-based verification (use if local pip builds fail on Windows)
---------------------------------------------------------------

Why
----
Some Python packages (pandas, numpy extensions) may need compilation on Windows and require Visual Studio build tools. To avoid local build issues, we provide a Dockerfile and a CI workflow that builds and runs the project in a clean Ubuntu environment.

Quick local test (requires Docker Desktop):

```bash
cd projects/crosscloud-data-pipeline
docker build -t crosscloud-pipeline:local .
docker run --rm crosscloud-pipeline:local python src/generator.py
```

This replicates what the CI will do on GitHub Actions and ensures the project is buildable in a clean Linux environment.
