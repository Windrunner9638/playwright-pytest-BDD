import pytest
from playwright.sync_api import expect
from pytest_bdd import given, when, then, scenarios, parsers

from pages.base_page import BasePage
from utils import Urls

scenarios('../features/common.feature')

@pytest.fixture
def base_page(playwright_page):
    return BasePage(playwright_page)


@when(parsers.parse("user {action} '{element_name}'"))
def user_interacts_with_element(base_page, action, element_name):
    element = base_page.map_elements(element_name)
    if action == "hovers over":
        element.hover()
    elif action == "clicks on":
        element.click()
    else:
        raise ValueError(f"Unknown action: {action}")

@then(parsers.parse("the '{element_name}' is {display_mode}"))
def element_is_displayed(base_page, element_name, display_mode):
    match display_mode:
        case "displayed":
            expect(base_page.map_elements(element_name)).to_be_visible()
        case "hidden":
            expect(base_page.map_elements(element_name)).to_be_hidden()
        case _:
            raise ValueError(f"Unknown display mode: {display_mode}")

@then(parsers.parse("the '{element_name}' is not displayed"))
def element_is_displayed(base_page, element_name):
    expect(base_page.map_elements(element_name)).to_not_be_visible()

@then(parsers.parse("{menu_type} mega-menu contains the following items: {expected_items}"))
def mega_menu_containing_items(base_page, menu_type, expected_items):
    expected_items = [item.strip() for item in expected_items.split(',')]
    menu_map = {
        "left": base_page.get_left_mega_menu_names(),
        "sub": base_page.get_sub_menu_category_names()
    }
    actual_items = menu_map.get(menu_type)
    assert actual_items == expected_items, f"Expected {expected_items} but found {actual_items} in the {menu_type} mega-menu."

@then(parsers.parse("{button_name} button is displayed in the right mega-menu"))
def sub_menu_containing_items(base_page, button_name):
    assert base_page.get_right_mega_menu_button_name() == button_name, f'Expected button {button_name} but found {base_page.get_right_mega_menu_button_name()}.'

@then(parsers.parse("cart counter is {quantity}"))
def login_popup_is_displayed(base_page, quantity):
    assert base_page.get_cart_counter() == quantity, f'Expected cart counter to be {quantity}, but got {base_page.get_cart_counter()}'

@then(parsers.parse("{element_name} contains correct link"))
def check_link(base_page, element_name):
    links_mapping = {
        'Just In': Urls.JUST_IN_URL,
        'Last Chance': Urls.LAST_CHANCE_URL,
    }
    assert base_page.get_link(element_name) == links_mapping[element_name]