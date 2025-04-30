# Test Cases: Currency Conversion Verification

## Test Case 1: Verify currency conversion via XE website and Windows Calculator

- **Test Case ID**: TC_001
- **Title**: Validate that conversion from RSD to all target currencies is accurate
- **Preconditions**:
  - Internet connection is active
  - XE web page is accessible
  - Windows Calculator can be accessed


- **Test Steps**:
  1. Open XE exchange site
  2. Set From currency field to RSD
  3. Set To currency field to target currency (e.g. USD, EUR, GBP...)
  4. Enter predefined amount in Amounts field (e.g. 1000, 2500, 5000)
  5. Record conversion result
  6. Repeat conversion process for all predefined amounts and currencies
  7. Round results to 3 decimal digits
  8. Save results to web_results.txt file 
  9. Start windows calculator
  10. Convert all amounts to predefined currencies
  11. Save results to calculator_results.txt file, rounded to 3 decimal digits
  12. Compare both result files from web and calculator

  
- **Expected Result**:
  - Result from XE and Calculator must match
  
- **Actual Result**:
  - (To be filled after execution)
  
- **Status**: Pass / Fail

- **Notes**:
  - If mismatch, log rate and amounts to a file

  

## Test Case 2: Verify currency conversion via WISE website and Windows Calculator
- **Test Case ID**: TC_002
- **Title**: Validate that conversion from RSD to all target currencies is accurate
- **Preconditions**:
  - Internet connection is active
  - XE web page is accessible
  - Windows Calculator can be accessed
  
- **Test Steps**:
  1. Open XE exchange site
  2. Set From currency field to RSD
  3. Set To currency field to target currency (e.g. USD, EUR, GBP...)
  4. Enter predefined amount in Amounts field (e.g. 1000, 2500, 5000)
  5. Record conversion result
  6. Repeat conversion process for all predefined amounts and currencies
  7. Round results to 3 decimal digits
  8. Save results to web_results.txt file 
  9. Start windows calculator
  10. Convert all amounts to predefined currencies
  11. Save results to calculator_results.txt file, rounded to 3 decimal digits
  12. Compare both result files from web and calculator
  
- **Expected Result**:
  - Result from WISE and Windows Calculator must match
  
- **Actual Result**:
  - (To be filled after execution)
  
- **Status**: Pass / Fail

- **Notes**:
  - If mismatch, log rate and amounts to a file