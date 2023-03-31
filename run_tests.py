import datetime
import pytest

now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

pytest.main(["-v", f"--html=report_{now}.html", "tests/"])

