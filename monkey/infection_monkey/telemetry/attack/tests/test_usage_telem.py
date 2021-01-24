import pytest

from common.utils.attack_utils import ScanStatus, UsageEnum
from infection_monkey.telemetry.attack.usage_telem import UsageTelem


@pytest.fixture
def mock_data():
    status = ScanStatus.USED
    technique = 'T1035'
    usage = UsageEnum.SMB
    telem = UsageTelem(technique, status, usage)
    return {'status': status,
            'technique': technique,
            'usage': usage,
            'telem': telem}


class TestUsageTelem:
    def test_telem_category(self, mock_data):
        assert mock_data['telem'].telem_category == 'attack'

    def test_get_data(self, mock_data):
        expected_data = {
            'status': mock_data['status'].value,
            'technique': mock_data['technique'],
            'usage': mock_data['usage'].name
        }
        actual_data = mock_data['telem'].get_data()
        assert actual_data == expected_data
