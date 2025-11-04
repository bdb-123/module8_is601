# FastAPI Calculator Application 🧮

A comprehensive FastAPI-based calculator application with full test coverage including unit tests, integration tests, and end-to-end tests using Playwright. This project demonstrates REST API development, automated testing, logging, and CI/CD with GitHub Actions.

## 🎯 Project Overview

This project implements a web-based calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division) through a REST API built with FastAPI. The application includes:

- **FastAPI Backend**: RESTful API endpoints for arithmetic operations
- **Interactive Web Interface**: HTML/CSS/JavaScript frontend
- **Comprehensive Testing**: Unit, integration, and E2E tests
- **Logging**: Application-wide logging for operations and errors
- **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions
- **Containerization**: Docker support for easy deployment

## 📋 Features

- ✅ Four arithmetic operations: Add, Subtract, Multiply, Divide
- ✅ Input validation and error handling
- ✅ Division by zero protection
- ✅ Interactive web interface
- ✅ RESTful API endpoints
- ✅ 100% test coverage
- ✅ Automated CI/CD pipeline
- ✅ Docker containerization

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**:
```bash
git clone <your-repo-url>
cd module8_is601
```

2. **Create and activate virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers** (for E2E tests):
```bash
playwright install
```

### Running the Application

**Start the FastAPI server**:
```bash
python main.py
```

The application will be available at: `http://127.0.0.1:8000`

## 🧪 Testing

This project includes three levels of testing:

### Unit Tests
Tests for individual arithmetic functions in `app/operations/__init__.py`:
```bash
pytest tests/unit/ -v
```

### Integration Tests
Tests for FastAPI API endpoints:
```bash
pytest tests/integration/ -v
```

### End-to-End Tests
Browser-based tests using Playwright:
```bash
pytest tests/e2e/ -v
```

### Run All Tests with Coverage
```bash
pytest tests/unit/ tests/integration/ --cov=app --cov-report=term-missing --cov-report=html
```

View the HTML coverage report by opening `htmlcov/index.html` in your browser.

## 🔌 API Endpoints

### Base URL
`http://127.0.0.1:8000`

### Endpoints

#### 1. **GET /** - Homepage
Returns the calculator web interface.

#### 2. **POST /add** - Addition
```json
Request:
{
  "a": 10,
  "b": 5
}

Response:
{
  "result": 15
}
```

#### 3. **POST /subtract** - Subtraction
```json
Request:
{
  "a": 10,
  "b": 5
}

Response:
{
  "result": 5
}
```

#### 4. **POST /multiply** - Multiplication
```json
Request:
{
  "a": 10,
  "b": 5
}

Response:
{
  "result": 50
}
```

#### 5. **POST /divide** - Division
```json
Request:
{
  "a": 10,
  "b": 2
}

Response:
{
  "result": 5.0
}

Error (Division by Zero):
{
  "error": "Cannot divide by zero!"
}
```

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -t fastapi-calculator .
```

### Run Docker Container
```bash
docker run -p 8000:8000 fastapi-calculator
```

### Using Docker Compose
```bash
docker-compose up
```

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

### Workflow Stages

1. **Test Stage**:
   - Runs unit tests
   - Runs integration tests
   - Runs E2E tests
   - Generates coverage reports

2. **Security Stage**:
   - Builds Docker image
   - Runs Trivy vulnerability scanner
   - Checks for critical and high severity issues

3. **Deploy Stage**:
   - Pushes Docker image to Docker Hub
   - Supports multi-platform builds (amd64, arm64)
   - Only runs on main branch

### Viewing GitHub Actions

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. View the latest workflow runs

## 📊 Test Coverage

Current test coverage: **100%**

- **Unit Tests**: 21 tests covering all arithmetic operations
- **Integration Tests**: 5 tests covering all API endpoints
- **E2E Tests**: 3 tests covering user interface interactions

## 📁 Project Structure

```
module8_is601/
├── .github/
│   └── workflows/
│       └── test.yml           # GitHub Actions CI/CD pipeline
├── app/
│   └── operations/
│       └── __init__.py        # Arithmetic operations
├── templates/
│   └── index.html             # Web interface
├── tests/
│   ├── unit/
│   │   └── test_calculator.py # Unit tests
│   ├── integration/
│   │   └── test_fastapi_calculator.py # Integration tests
│   └── e2e/
│       ├── conftest.py        # Playwright fixtures
│       └── test_e2e.py        # E2E tests
├── main.py                    # FastAPI application
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose configuration
└── README.md                  # This file
```

## � Screenshots

### 1. Application Running in Browser
*TODO: Add screenshot of the calculator web interface*

### 2. Successful GitHub Actions Workflow
*TODO: Add screenshot of successful GitHub Actions run*

### 3. Test Coverage Report
*TODO: Add screenshot of coverage report*

## 🎓 Learning Outcomes

This project demonstrates:

- **CLO10**: Create, Consume and Test REST APIs using Python
  - Created RESTful API endpoints using FastAPI
  - Implemented comprehensive testing strategies
  - Utilized proper error handling and validation
  - Integrated logging for debugging and monitoring

## 🛠️ Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Pytest**: Testing framework
- **Playwright**: Browser automation for E2E testing
- **Uvicorn**: ASGI server for FastAPI
- **Docker**: Containerization
- **GitHub Actions**: CI/CD automation
- **Jinja2**: Template engine for HTML rendering

## 📝 Assignment Submission Checklist

- [x] All arithmetic operations implemented and working
- [x] Unit tests written for all functions in operations.py
- [x] Integration tests written for all API endpoints
- [x] End-to-end tests implemented using Playwright
- [x] Logging implemented throughout the application
- [x] GitHub Actions workflow configured and working
- [ ] Screenshot of successful GitHub Actions workflow
- [ ] Screenshot of application running in browser
- [ ] GitHub repository link ready for submission

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# 📦 Detailed Setup Instructions

---

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

# 🧩 2. Install and Configure Git

## Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

---

## Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

## Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

# 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

# 🛠️ 4. Install Python 3.10+

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---

## Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🐳 5. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

## Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

## Build Docker Image

```bash
docker build -t <image-name> .
```

## Run Docker Container

```bash
docker run -it --rm <image-name>
```

---

# 🚀 6. Running the Project

- **Without Docker**:

```bash
python main.py
```

(or update this if the main script is different.)

- **With Docker**:

```bash
docker run -it --rm <image-name>
```

---

# 📝 7. Submission Instructions

After finishing your work:

```bash
git add .
git commit -m "Complete Module X"
git push origin main
```

Then submit the GitHub repository link as instructed.

---

# 🔥 Useful Commands Cheat Sheet

| Action                         | Command                                          |
| ------------------------------- | ------------------------------------------------ |
| Install Homebrew (Mac)          | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Install Git                     | `brew install git` or Git for Windows installer |
| Configure Git Global Username  | `git config --global user.name "Your Name"`      |
| Configure Git Global Email     | `git config --global user.email "you@example.com"` |
| Clone Repository                | `git clone <repo-url>`                          |
| Create Virtual Environment     | `python3 -m venv venv`                           |
| Activate Virtual Environment   | `source venv/bin/activate` / `venv\Scripts\activate.bat` |
| Install Python Packages        | `pip install -r requirements.txt`               |
| Build Docker Image              | `docker build -t <image-name> .`                |
| Run Docker Container            | `docker run -it --rm <image-name>`               |
| Push Code to GitHub             | `git add . && git commit -m "message" && git push` |

---

# 📋 Notes

- Install **Homebrew** first on Mac.
- Install and configure **Git** and **SSH** before cloning.
- Use **Python 3.10+** and **virtual environments** for Python projects.
- **Docker** is optional depending on the project.

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
