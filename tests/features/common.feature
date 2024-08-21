Feature: Common
  # Enter feature description here
  Background:
    Given the 'home' page is opened
    And user accepts cookie policy

  Scenario: All elements in the header are correctly displayed
    Then the 'company logo' is displayed
    And the 'search input' is displayed
    And the 'account button' is displayed
    And the 'support button' is displayed
    And the 'cart button' is displayed
    And the 'cart counter' is displayed
    And cart counter is 0
    And the 'Last Chance link' is displayed
    And Last Chance link contains correct link
    And the 'Just In link' is displayed
    And Just In link contains correct link
    And the 'Franchise menu' is displayed
    And the 'Video Games menu' is displayed
    And the 'Merchandise menu' is displayed
    And the 'FFXIV Merchandise menu' is displayed
    And the 'Rewards link' is displayed
    And the 'Offers link' is displayed

  Scenario: Expandable mega-menus contain correct items
    When user hovers over 'Franchise menu'
    Then the 'mega-menu' is displayed
    And left mega-menu contains the following items: FINAL FANTASY XVI, FINAL FANTASY, FINAL FANTASY XIV Online, FINAL FANTASY VII, KINGDOM HEARTS, NieR, DRAGON QUEST, Life is Strange, The World Ends With You, Mana
    And All Franchise button is displayed in the right mega-menu
    When user hovers over 'Video Games menu'
    Then the 'mega-menu' is displayed
    And left mega-menu contains the following items: Pre-Orders
    And sub mega-menu contains the following items: GENRE, FRANCHISE, PLATFORM
    And All Video Games button is displayed in the right mega-menu
    When user hovers over 'Merchandise menu'
    Then the 'mega-menu' is displayed
    And left mega-menu contains the following items: Pre-Orders, Apparel, Books
    And sub mega-menu contains the following items: ACTION FIGURES, PLUSH, JEWELRY, ACCESSORIES, HOME GOODS, MUSIC, TABLE TOP
    And All Merchandise button is displayed in the right mega-menu
    When user hovers over 'FFXIV Merchandise menu'
    Then the 'mega-menu' is displayed
    And left mega-menu contains the following items: FAN FEST 2023 - 2024 ITEMS, FEATURED ITEMS, Available Now, View all
    And All FFXIV MERCHANDISE button is displayed in the right mega-menu