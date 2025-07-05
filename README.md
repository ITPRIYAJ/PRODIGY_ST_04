# PRODIGY_ST_04
Automate and validate the login functionality across multiple browsers and operating systems using Selenium WebDriver and BrowserStack cloud infrastructure. 
Details:  Application under Test:  https://demowebshop.tricentis.com/ (Demo WebShop)  Or https://www.saucedemo.com/ (SauceDemo)
# 🚀 Cross-Browser Automated Testing with Selenium, PyTest & BrowserStack

# 

This project demonstrates **cross-browser automation testing** using:

✅ Selenium WebDriver  
✅ PyTest Framework  
✅ BrowserStack Cloud Infrastructure

Tests validate login functionality across **Chrome, Firefox, Edge, Safari** on different OS platforms using BrowserStack.

* * *

## 📁 Project Structure

# 

`regression_testing/ ├── tests/ │   └── test_crossbrowser.py    # PyTest file with parameterized cross-browser tests ├── venv/                       # Python Virtual Environment ├── requirements.txt            # Dependencies list └── README.md                    # Project documentation`

* * *

## 🌐 Prerequisites

# 

*   Python 3.8+
    
*   Valid BrowserStack Account
    
*   Selenium 4.x
    
*   PyTest 8.x
    

* * *

## 🔑 BrowserStack Credentials

# 

Update your `test_crossbrowser.py` with your BrowserStack credentials:

python

`USERNAME = "YOUR_USERNAME" ACCESS_KEY = "YOUR_ACCESS_KEY"`

You can obtain credentials from: https://www.browserstack.com/accounts/settings

* * *

## ⚙️ Install Dependencies

# 

`pip install -r requirements.txt`

**`requirements.txt`** Example:

txt

`selenium==4.19.0 pytest==8.4.1`

* * *

## 🧪 Run Cross-Browser Tests

# 

Execute tests via:

`pytest tests/test_crossbrowser.py`

* * *

## 🖥️ Browsers Tested

# 

| Browser | Version | OS |
| --- | --- | --- |
| Chrome | Latest | Windows 10 |
| Firefox | Latest | macOS Monterey |
| Safari | Latest | macOS Big Sur |
| Edge | Latest | Windows 11 |

* * *

## ✅ Features

# 

*   Cloud-based testing using BrowserStack
    
*   Supports multiple browsers & OS combinations
    
*   Selenium with PyTest parameterization
    
*   Login functionality tested for:
    
    *   `https://demowebshop.tricentis.com/` or
        
    *   `https://www.saucedemo.com/`
        

* * *

## ⚠️ Notes

# 

*   Some browsers like Safari may require specific BrowserStack configurations
    
*   `DeprecationWarnings` related to URL authentication are expected in Selenium 4.x
    

* * *

## 📢 Future Enhancements

# 

*   Integrate with CI/CD pipelines (GitHub Actions, Jenkins)
    
*   Extend tests for other workflows (Registration, Purchase flow)
    
*   Handle Selenium best practices for capabilities
    

* * *

## 🤝 Acknowledgements

# 

Powered by:

*   [Selenium WebDriver](https://www.selenium.dev/)
    
*   [PyTest](https://pytest.org/)
    
*   [BrowserStack](https://www.browserstack.com/)
    

* * *

## 💻 Developed By

# 

`Priyadharshini J` | Demo for BrowserStack Cross-Browser Automation 🚀
