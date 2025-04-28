import pytest
from datetime import datetime
from pathlib import Path
import shutil
import webbrowser

from utils.logger import logger

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

REPORTS_DIR = "reports"
ARCHIVE_DIR = "reports_archive"
HTML_REPORT = "report.html"

pytest.main()

html_report = Path(__file__).parent / Path(REPORTS_DIR) / "report.html"

reports_archive_directory = Path(__file__).parent / Path(REPORTS_DIR) / ARCHIVE_DIR / timestamp
reports_archive_directory.mkdir(parents=True, exist_ok=True)

html_archive_report_filename = reports_archive_directory / f"report_{timestamp}.html"

shutil.copy2(html_report, html_archive_report_filename)
logger.info(f"Reports have been copied to {reports_archive_directory} with timestamp {timestamp}.")

webbrowser.open(f"file://{html_report}")
