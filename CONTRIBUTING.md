# Contributing to Python Chess

Thank you for investing your time in improving this project!

## Ground Rules

1. Treat everyone with respect and follow our [Code of Conduct](CODE_OF_CONDUCT.md).
2. **One issue at a time:** Please comment on an issue to get it assigned to you before starting work to avoid duplicate effort.
3. Keep pull requests (PRs) focused on a single change or feature.

---

## Development Workflow

### 1. Fork & Clone
Fork the repository on GitHub, then clone your fork locally:
```
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>
```
### 2. Create a branch
Branch off ```main``` with a descriptive name that reflects the change or feature you are working on.
```
git checkout -b feature/legal-move-dots
# or
git checkout -b fix/bot-delay
```
### 3. Setup virtual enviroment
```
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 4. Code standards
- Adhere to standard [PEP 8](https://peps.python.org/pep-0008/) style guidelines.
- Use explicit type hints for new functions where feasible.
- Do not check in unused binary files or oversized media assets into Git without prior dicussion and approval.

### 5. Submitting a Pull Request
1. Commit your changes with clear messages: ```git commit -m "feat: add legal move target circles in pygame"```
2. Push to your fork: ```git push origin feature/legal-move-dots```
3. Open a Pull Request pointing to the ```main``` branch.
4. Reference the issue number in the PR description if applicable (e.g. ```Closes #123```).