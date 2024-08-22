import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from pytest_bdd import given, parsers, then

from utils import Urls


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


@given(parsers.parse("the '{page_name}' page is opened"))
@then(parsers.parse("the '{page_name}' page is opened"))
def page_is_opened(playwright_page, page_name):
    page_mapping = {
        "home": Urls.HOME_URL,
        "Just In": Urls.JUST_IN_URL,
        "Last Chance": Urls.LAST_CHANCE_URL
    }
    if page_name in page_mapping:
        playwright_page.goto(page_mapping[page_name])
    else:
        raise ValueError(f"Unknown page: {page_name}")


@given("user accepts cookie policy")
def accept_cookie_policy(playwright_page):
    playwright_page.get_by_role("button", name="Accept").click()