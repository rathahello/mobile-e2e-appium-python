# Mobile App E2E Test Automation (Appium + Python + Pytest)

A robust End-to-End (E2E) mobile test automation framework built with **Python**, **Appium**, and **Pytest**, implementing the **Page Object Model (POM)** design pattern.

---

## 📋 Features

- **Page Object Model (POM)**: Decoupled UI page representations and test assertions for maintainability.
- **Data-Driven Testing (DDT)**: Externalized test data in JSON format (`data/` directory).
- **Automated Artifacts**: Built-in screenshot and screen recording capture on test failures/events.
- **Custom Gestures**: Reusable UI automator actions including smooth scrolling, gestures, and accessibility locators.
- **Reporting**: Compatible with `pytest-html` for test execution reporting.

---

## 🏗️ Project Structure

```text
├── data/                       # Test data and environment configurations
│   ├── apk.json                # Target APK metadata
│   ├── credentials.json        # Test credentials (login/auth)
│   ├── devices.json            # Device capabilities (emulator & real devices)
│   └── facility_app/           # Module-specific test data (ads, registration, etc.)
├── features/                   # Test scenarios and execution suites
│   ├── facilityApp/            # App-specific test cases (test_001 to test_009)
│   └── test_web_app.py         # Mobile web browser test scenarios
├── pages/                      # Page Object classes (POM)
│   ├── AdsPage.py              # Advertisement creation, update, deletion
│   ├── Custom.py               # Shared gestures, screenshots, helper utilities
│   ├── LoginPage.py            # Authentication & session management
│   ├── Register.py             # User registration flow
│   ├── UserManagement.py       # Admin actions & approvals
│   └── UserProfile.py          # Account settings & deletion
├── screenshots/                # Captured test screenshots (git-ignored)
├── utils/                      # Driver initialization & environment helpers
│   ├── facility_app.py         # Appium driver setup for facility app
│   ├── get_webdriver.py        # Generic webdriver initializers
│   └── web_app.py              # Chrome mobile browser driver setup
├── .gitignore                  # Git ignore rules for virtualenv, logs, APKs
├── pytest.ini                  # Pytest execution configuration
├── requirements.txt            # Python package dependencies
└── README.md                   # Project documentation
```

---

## 🛠️ Prerequisites

Before running the tests, ensure you have the following installed and configured:

1. **Python**: 3.10 or higher
2. **Node.js & Appium 2.x**:
   ```bash
   npm install -g appium
   appium driver install uiautomator2
   ```
3. **Android SDK**: `ANDROID_HOME` configured in environment variables with `platform-tools` (`adb`) in `PATH`.
4. **Java JDK**: JDK 11 or higher with `JAVA_HOME` configured.
5. **Real Device or Android Emulator**: Connected via USB or running via Android Studio.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/rathahello/mobile-e2e-appium-python.git
cd mobile-e2e-appium-python
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Device & Test Data
- Update `data/devices.json` with your device name and Android version:
  ```json
  {
    "virtual": {
      "device_name": "emulator-5554",
      "version": "11"
    },
    "real": {
      "device_name": "<YOUR_DEVICE_ID>",
      "version": "<ANDROID_VERSION>"
    }
  }
  ```
- Place target APK inside `utils/apk/` and verify the filename matches `data/apk.json`.
- Update credentials in `data/credentials.json`.

---

## 🧪 Running Tests

### Start Appium Server
```bash
appium --port 4723
```

### Run Test Suites
```bash
# Run all tests
pytest

# Run a specific test module
pytest features/facilityApp/test_001_login_logout.py

# Run tests with HTML report generation
pytest --html=reports/report.html --self-contained-html
```

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).