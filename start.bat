@echo off
SET "root=%~dp0"
@echo root: %root%
call %root%.venv\Scripts\activate

python run_tests.py
