import pytest

from common.utils.attack_utils import ScanStatus
from infection_monkey.model import VictimHost
from infection_monkey.telemetry.attack.victim_host_telem import VictimHostTelem


@pytest.fixture
def mock_data():
    machine = VictimHost('127.0.0.1')
    status = ScanStatus.USED
    technique = 'T1210'
    telem = VictimHostTelem(technique, status, machine)
    return {'machine': machine,
            'status': status,
            'technique': technique,
            'telem': telem}


class TestVictimHostTelem:
    def test_telem_category(self, mock_data):
        assert mock_data['telem'].telem_category == 'attack'

    def test_get_data(self, mock_data):
        expected_data = {
            'machine': {
                'domain_name': mock_data['machine'].domain_name,
                'ip_addr': mock_data['machine'].ip_addr
            },
            'status': mock_data['status'].value,
            'technique': mock_data['technique']
        }
        actual_data = mock_data['telem'].get_data()
        assert actual_data == expected_data
