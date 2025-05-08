@echo off
SET "root=%~dp0"
@echo root: %root%
call %root%.venv\Scripts\activate.bat

python run_tests.py
