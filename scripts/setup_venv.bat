@echo off

cd /d %~dp0
cd ..

if not exist requirements.txt (
    echo Error: requirements.txt not found in the parent directory.
    pause
    exit /b 1
)

python -m venv .venv

call .venv\Scripts\activate

pip install -r requirements.txt

echo Batch job completed successfully!
