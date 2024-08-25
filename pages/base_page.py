from playwright.sync_api import Locator

from conftest import playwright_page


class BasePage:
    headerLogo = '.eyebrow-logo'
    headerSearch = '.eyebrow-search:not(.eyebrow-mobile-search)'
    headerAccountButton = '.eyebrow-user'
    headerSupportButton = '.eyebrow-support'
    headerCartButton = '.eyebrow-cart'
    cartCounter = '.eyebrow-cart span'
    lastChanceLink = '[id="eyebrow-last chance"] a'
    justInLink = '[id="eyebrow-just in"] a'
    franchiseMenuItem = '[id="eyebrow-franchise"]'
    videoGamesMenuItem = '[id="eyebrow-video games"]'
    merchandiseMenuItem = '[id="eyebrow-merchandise"]'
    ffXIVMerchandiseMenuItem = '[id="eyebrow-ffxiv merchandise"]'
    rightArrow = '.eyebrow-right-arrow'
    leftArrow = '.eyebrow-left-arrow'
    rewardsLink = '.eyebrow-rewards'
    offersLink = '.eyebrow-offers'
    megaMenu = '.eyebrow-megamenu'
    leftMegaMenuItems = 'ul.eyebrow-megamenu-left a'
    subMegaMenuCategories = 'ul.eyebrow-megamenu-sub h4'
    rightMegaMenuButton = '.eyebrow-megamenu-all-btn'
    loginPopup = '.eyebrow-login-body'
    cartPreview = '.cart-preview-inner'
    cartPreviewTitle = '.preview-cart-titles'
    cartPreviewCloseButton = '.previewCart-icon-close'
    previewCartEmptyBody = '.previewCart-emptyBody'
    closeButton = '.eyebrow-nav-close',
    loginButton = '.eyebrow-login-btn',
    loginText = '.eyebrow-login-text:not(.why-join)',
    joinButton = '.eyebrow-join-btn',
    joinText = '.why-join'
    joinMarkerText = '.eyebrow-login-body li'
    
    def __init__(self, playwright_page):
        self.page = playwright_page
        
    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def get_cart_preview_title(self):
        return self.find(BasePage.cartPreviewTitle).text_content()

    def get_right_mega_menu_button_name(self):
        return self.find(BasePage.rightMegaMenuButton).text_content()

    def get_left_mega_menu_names(self):
        return self.find(BasePage.leftMegaMenuItems).all_inner_texts()

    def get_sub_menu_category_names(self):
        return self.find(BasePage.subMegaMenuCategories).all_inner_texts()

    def get_cart_counter(self):
        return self.find(BasePage.cartCounter).text_content()

    def map_elements(self, element_name):
        element_mapping = {
            'company logo': BasePage.headerLogo,
            'search input': BasePage.headerSearch,
            'account button': BasePage.headerAccountButton,
            'support button': BasePage.headerSupportButton,
            'cart button': BasePage.headerCartButton,
            'Last Chance': BasePage.lastChanceLink,
            'Just In': BasePage.justInLink,
            'Franchise menu': BasePage.franchiseMenuItem,
            'Video Games menu': BasePage.videoGamesMenuItem,
            'Merchandise menu': BasePage.merchandiseMenuItem,
            'FFXIV Merchandise menu': BasePage.ffXIVMerchandiseMenuItem,
            'right arrow': BasePage.rightArrow,
            'left arrow': BasePage.leftArrow,
            'Rewards': BasePage.rewardsLink,
            'Offers': BasePage.offersLink,
            'mega-menu': BasePage.megaMenu,
            'mega-menu button': BasePage.rightMegaMenuButton,
            'cart counter': BasePage.cartCounter,
            'login popup': BasePage.loginPopup,
            'close button': BasePage.closeButton,
            'login button': BasePage.loginButton,
            'login text': BasePage.loginText,
            'join button': BasePage.joinButton,
            'join marker text': BasePage.joinMarkerText,
            'join text': BasePage.joinText,
        }

        if element_name in element_mapping:
            return self.find(element_mapping[element_name])
        else:
            raise ValueError(f"Unknown element: {element_name}")

    def get_link(self, element_name):
        element = self.map_elements(element_name)
        return element.get_attribute('href')
