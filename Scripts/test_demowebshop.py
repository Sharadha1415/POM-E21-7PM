from POM.homepage import HomePage
from POM.loginpage import LoginPage
from POM.desktop_page import DesktopPage
from POM.simplecomputer_page import SimpleComputerPage
from POM.cartpage import CartPage

from utilities.excel_utlility import excel_data

path = r'C:\Users\Ramya\PycharmProjects\POM-Feb11-7PM-E21\external_files\testdata.xlsx'
data = excel_data(path, 'login_data')
## {'invalid_email': 'abcdefgh@gmail.com', 'invalid_pwd': 'abc@12345', 'valid_email': 'steve.jobs123@gmail.com', 'valid_pwd': 'stevejobs', 'sort': 'Price: Low to High', 'view': 'List', 'country': 'India'}


def test_unsucessfull_login(setup):
    hp = HomePage(setup)
    lp = LoginPage(setup)

    hp.validate_homepage()
    hp.click_on_login()
    lp.enter_email(data['invalid_email'])
    lp.enter_password(data['invalid_pwd'])
    lp.click_on_login_btn()
    lp.validate_unsucessfull_msg()


def test_buy_simp_comp(setup):
    hp = HomePage(setup)
    lp = LoginPage(setup)
    dp = DesktopPage(setup)
    scp = SimpleComputerPage(setup)
    cp = CartPage(setup)

    hp.validate_homepage()
    hp.click_on_login()
    lp.enter_email(data['valid_email'])
    lp.enter_password(data['valid_pwd'])
    lp.click_on_login_btn()
    hp.validate_logout()
    hp.hover_to_computers()
    hp.click_on_desktop()
    dp.selecting_sortby(data['sort'])
    dp.selecting_view(data['view'])
    dp.scroll_pagedown()
    dp.click_on_simp_computer()
    scp.click_on_processor()
    scp.click_on_add_to_cart()
    scp.scroll_to_home()
    scp.click_on_shopping_cart()
    cp.select_country(data['country'])
    cp.click_terms_conditions()
    cp.click_on_checkout()







































