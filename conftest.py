import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from pytest_bdd import given, parsers, then

from utils import Urls


@pytest.fixture
def shared_data():
    return {}


@pytest.fixture
def playwright_page(page: Page):
    yield page
    page.close()


@pytest.fixture
def recordable_page(browser: Browser):
    context = browser.new_context(record_video_dir='video/')
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    context.tracing.start(name='playwright', screenshots=True, snapshots=True, sources=True)
    yield
    context.tracing.stop(path='trace.zip')
