# How to Push to GitHub

## Step-by-Step Guide

### Step 1: Make Sure Sensitive Files Are Ignored

First, ensure your `.gitignore` file excludes sensitive data. Create/update `.gitignore`:

```bash
cd /mnt/c/Users/sarat/OneDrive/Documents/self_learning/RAG/RAG
```

The `.gitignore` should already exist, but verify it includes:
- `.env` (contains your API keys - **NEVER commit this!**)
- `venv/` (virtual environment)
- `data/` (data files)
- `__pycache__/` (Python cache)
- `*.pyc` (compiled Python files)

### Step 2: Check What Will Be Committed

```bash
# See what files will be added
git status

# See which files are ignored
git status --ignored
```

**IMPORTANT**: Make sure `.env` is NOT in the list of files to be committed!

### Step 3: Add Files to Git

```bash
# Add all files (except those in .gitignore)
git add .

# Or add files selectively:
git add src/
git add docs/
git add tests/
git add README.md
git add requirements.txt
git add setup.py
git add LICENSE
git add env.example
git add examples/
git add QUICKSTART.md
git add GETTING_STARTED.md
git add PROJECT_SUMMARY.md

# Verify what's staged
git status
```

### Step 4: Commit Your Changes

```bash
git commit -m "Initial commit: My Personal Agent RAG application

- Core RAG engine with ChromaDB vector store
- Vehicle diagnostics module with vision AI
- Resume analyzer with ATS optimization
- Resume builder with job-specific optimization
- User authentication system
- CLI interface
- Comprehensive documentation"
```

### Step 5: Push to GitHub

Since you already have a remote (origin/main), push your changes:

```bash
# Push to main branch
git push origin main
```

If you need to create a new repository on GitHub first:

1. Go to https://github.com/new
2. Create a new repository (don't initialize with README since you already have one)
3. Then run:

```bash
# If you need to set a new remote (only if creating new repo)
git remote remove origin  # Remove old remote if needed
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## Important Security Notes

### ⚠️ NEVER COMMIT:

- `.env` file (contains API keys and secrets)
- `venv/` directory (virtual environment)
- `data/` directory (may contain sensitive data)
- Any file with API keys or passwords

### ✅ ALWAYS COMMIT:

- `env.example` (template file without real keys)
- Source code (`src/`)
- Documentation (`docs/`, README files)
- Configuration files (`requirements.txt`, `setup.py`)
- Tests (`tests/`)
- `.gitignore`

## Quick Command Summary

```bash
# Navigate to project
cd /mnt/c/Users/sarat/OneDrive/Documents/self_learning/RAG/RAG

# Check status
git status

# Add files (make sure .env is NOT included!)
git add .

# Verify .env is NOT in the staged files
git status

# Commit
git commit -m "Your commit message here"

# Push
git push origin main
```

## If You Accidentally Added .env

If you accidentally added `.env` to git:

```bash
# Remove it from staging (but keep the file locally)
git reset HEAD .env

# If you already committed it, remove it from history:
git rm --cached .env
git commit -m "Remove .env file from repository"

# Then add .env to .gitignore and commit that
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Add .env to .gitignore"

# Push the fix
git push origin main
```

## Verify Before Pushing

Before pushing, double-check:

```bash
# See what will be committed
git status

# See the actual diff
git diff --cached

# Make sure .env is not in the list!
```

## Optional: Create a Release

Once pushed, you can create a release on GitHub:

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Tag: `v1.0.0`
4. Title: `My Personal Agent v1.0.0`
5. Description: Copy from PROJECT_SUMMARY.md
6. Publish release

## Your Repository Should Include

```
✅ src/                    # Source code
✅ docs/                   # Documentation
✅ tests/                  # Unit tests
✅ examples/               # Example files
✅ README.md               # Main readme
✅ QUICKSTART.md           # Quick start guide
✅ GETTING_STARTED.md      # Getting started guide
✅ PROJECT_SUMMARY.md      # Project summary
✅ LICENSE                 # MIT License
✅ requirements.txt        # Dependencies
✅ setup.py                # Package setup
✅ env.example             # Environment template
✅ .gitignore              # Git ignore rules
❌ .env                    # NEVER commit this!
❌ venv/                   # Virtual environment
❌ data/                   # Data files
```

Happy coding! 🚀

