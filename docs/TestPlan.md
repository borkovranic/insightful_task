## Test Plan

### Project Name:
Insightful Task – Currency Conversion Test

### Objective:
Validating that conversion rates from the XE exchange website are accurate by comparing them to results from desktop calculator.

### Scope:
- Convert multiple amounts from RSD to USD and EUR
- Fetch conversion rates from XE
- Perform equivalent calculations in Windows Calculator
- Compare the results from both sources for consistency

### Tools:
- Python 3.x
- Pytest
- Playwright (for web interaction)
- pywinauto (for desktop automation)
- Windows Calculator

### Test Environment:
- Windows 10 or later
- Internet access

### Roles & Responsibilities:
- Test Automation Engineer: Design and execute automated test cases

### Entry Criteria:
- All required dependencies from requirements.txt file are installed
- Exchange websites are accesible
- Calculator desktop application is functional
- Test data (currencies, amounts, mappings) defined in configuration file

### Exit Criteria:
- Test cases executed
- No critical failures
- Logs and report are generated

### Risks:
- Calculator not responding
- Web page structure changes

### Deliverables:
- Test Plan
- Test Cases
- Pytest Report