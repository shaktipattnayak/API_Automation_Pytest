# API Automation (pytest)

A simple, user-friendly API automation test suite using pytest.

## Project structure

- `api_tests/` - contains tests organized by feature
- `config/config.yaml` - test configuration (base URL, etc.)
- `schema/` - JSON schemas used for validation
- `utils/` - helper modules (e.g., `client.py`)
- `validators/` - schema validation utilities
- `requirements.txt` - Python dependencies

---

## Prerequisites

- Python 3.11 or newer
- Git (optional)

---

## Setup (Windows example)

1. Clone the repo (if needed):

   ```bash
   git clone <repo-url>
   cd API_Automation_Pytest
   ```

2. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

3. Activate the virtual environment:

   - PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - CMD:
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   - Bash (WSL / macOS / Linux):
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Running tests

- Run the full test suite:

  ```bash
  pytest
  ```
- Run test with detail test information:
    ```bash
    pytest -vv -s
    ```
- Run with more output / stop on first failure:

  ```bash
  pytest -q -x
  ```

- Run a single test file:

  ```bash
  pytest api_tests/tests/posts/test_posts_positive.py
  ```

- Run a single test function:

  ```bash
  pytest api_tests/tests/posts/test_posts_positive.py::test_example
  ```

- Run tests matching a keyword:

  ```bash
  pytest -k "keyword"
  ```

- Show collected tests (no run):

  ```bash
  pytest --collect-only
  ```

Tips:
- Use `-s` to see print/log output in real time.
- Use `-m` to run tests by marker if markers are used.
- use `-vv` increases verbosity so every test is clearly identified.

---

## Configuration

The test configuration lives in `config/config.yaml`. Update values like the base URL or credentials there as needed.

---

## Troubleshooting

- If a test can't find the correct environment, ensure the virtual environment is activated.
- If dependencies are missing, re-run `pip install -r requirements.txt`.
- For schema validation issues, check the JSON schema files in `schema/`.
