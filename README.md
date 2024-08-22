# Playwright-Pytest-BDD
This project provides an example for testing a UI with Playwright, written in Python, using the Page Object Model design pattern and driven via BDD feature files through Pytest BDD.

## Getting Started
1. Install [pip](https://pypi.org/project/pip/) package manager;
2. Install Python (3.10+);
3. Install [JDK](https://corretto.aws/downloads/latest/amazon-corretto-11-x64-macos-jdk.pkg) (required for Allure);
4. Clone the repository;
5. Install project dependencies using the following command in Pycharm terminal: ``` pip install -r requirements.txt ```
6. Install Playwright browsers using the following command: ``` playwright install ```

### Running tests
```shell script
# Run all tests
   pytest
```

```shell script
# Run specific test suite
   pytest -m <suite_name>
```

### Generating Allure report
```shell script
allure serve allure_results
```
