# tests/conftest.py

import subprocess
import time
import pytest
import sys
import os
from playwright.sync_api import sync_playwright
import requests

@pytest.fixture(scope='session')
def fastapi_server():
    """
    Fixture to start the FastAPI server before E2E tests and stop it after tests complete.
    """
    # Get the correct Python executable
    python_executable = sys.executable
    
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    main_py = os.path.join(project_root, 'main.py')
    
    # Start FastAPI app with explicit Python path
    fastapi_process = subprocess.Popen(
        [python_executable, main_py],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Define the URL to check if the server is up
    server_url = 'http://127.0.0.1:8000/'
    
    # Wait for the server to start by polling the root endpoint
    timeout = 30  # seconds
    start_time = time.time()
    server_up = False
    
    print("Starting FastAPI server...")
    
    while time.time() - start_time < timeout:
        try:
            response = requests.get(server_url, timeout=2)
            if response.status_code == 200:
                server_up = True
                print("FastAPI server is up and running.")
                break
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            pass
        time.sleep(1)
    
    if not server_up:
        fastapi_process.terminate()
        # Try to get error output
        try:
            stdout, stderr = fastapi_process.communicate(timeout=2)
            print(f"Server stdout: {stdout.decode()}")
            print(f"Server stderr: {stderr.decode()}")
        except Exception as e:
            print(f"Could not get server output: {e}")
        raise RuntimeError("FastAPI server failed to start within timeout period.")
    
    yield
    
    # Terminate FastAPI server
    print("Shutting down FastAPI server...")
    fastapi_process.terminate()
    try:
        fastapi_process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        fastapi_process.kill()
        fastapi_process.wait()
    print("FastAPI server has been terminated.")

@pytest.fixture(scope="session")
def playwright_instance_fixture():
    """
    Fixture to manage Playwright's lifecycle.
    """
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance_fixture):
    """
    Fixture to launch a browser instance.
    """
    browser = playwright_instance_fixture.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """
    Fixture to create a new page for each test.
    """
    page = browser.new_page()
    yield page
    page.close()
