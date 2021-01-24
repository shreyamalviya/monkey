import pytest

from common.utils.attack_utils import ScanStatus
from infection_monkey.telemetry.attack.attack_telem import AttackTelem


@pytest.fixture
def mock_data():
    status = ScanStatus.USED
    technique = 'T1210'
    telem = AttackTelem(technique, status)
    return {'status': status,
            'technique': technique,
            'telem': telem}


class TestAttackTelem:
    def test_telem_category(self, mock_data):
        assert mock_data['telem'].telem_category == 'attack'

    def test_get_data(self, mock_data):
        expected_data = {
            'status': mock_data['status'].value,
            'technique': mock_data['technique']
        }
        actual_data = mock_data['telem'].get_data()
        assert actual_data == expected_data
