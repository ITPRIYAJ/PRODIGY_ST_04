import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

USERNAME = "itbpriyadharshin_FCtdpb"
ACCESS_KEY = "hH4Ef7qfeKG5zZoRtvqv"

browsers = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "buildName": "DemoWebShop_Login",
            "sessionName": "Login Test - Chrome"
        }
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Monterey",
            "buildName": "DemoWebShop_Login",
            "sessionName": "Login Test - Firefox"
        }
    }
]

@pytest.mark.parametrize("capabilities", browsers)
def test_login_cross_browser(capabilities):
    print(f"\n🔍 Running test on {capabilities['browserName']} ({capabilities['bstack:options']['os']} {capabilities['bstack:options']['osVersion']})")

    url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

    browser_name = capabilities["browserName"].lower()

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        pytest.skip(f"Unsupported browser: {capabilities['browserName']}")

    options.set_capability("browserName", capabilities["browserName"])
    options.set_capability("browserVersion", capabilities["browserVersion"])
    options.set_capability("bstack:options", capabilities["bstack:options"])

    driver = webdriver.Remote(command_executor=url, options=options)

    try:
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        assert "inventory" in driver.current_url, "❌ Login failed or unexpected redirect."

        print("✅ Login successful.")

    except NoSuchElementException as e:
        pytest.fail(f"❌ Element not found: {e}")

    finally:
        driver.quit()
