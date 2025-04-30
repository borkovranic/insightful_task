@echo off
SET "root=%~dp0"
@echo root: %root%
call %root%.venv\Scripts\Activate.bat

python run_tests.py
