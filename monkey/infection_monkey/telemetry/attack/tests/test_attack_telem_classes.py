import pytest

from common.utils.attack_utils import ScanStatus, UsageEnum
from infection_monkey.model import VictimHost
from infection_monkey.telemetry.attack.attack_telem import AttackTelem
from infection_monkey.telemetry.attack.usage_telem import UsageTelem
from infection_monkey.telemetry.attack.victim_host_telem import VictimHostTelem

MACHINE = VictimHost('127.0.0.1')
STATUS = ScanStatus.USED
TECHNIQUE = 'T9999'
USAGE = UsageEnum.SMB

MOCK_DATA = [
    (
        UsageTelem(TECHNIQUE, STATUS, USAGE),
        {'status': STATUS.value,
         'technique': TECHNIQUE,
         'usage': USAGE.name}
    ),
    (
        AttackTelem(TECHNIQUE, STATUS),
        {'status': STATUS.value,
         'technique': TECHNIQUE}
    ),
    (
        VictimHostTelem(TECHNIQUE, STATUS, MACHINE),
        {'machine': {'domain_name': MACHINE.domain_name,
                     'ip_addr': MACHINE.ip_addr},
         'status': STATUS.value,
         'technique': TECHNIQUE}
    )
]


@pytest.mark.parametrize('telem, _', MOCK_DATA)
def test_telem_category(telem, _):
    assert telem.telem_category == 'attack'


@pytest.mark.parametrize('telem, expected_data', MOCK_DATA)
def test_get_data(telem, expected_data):
    actual_data = telem.get_data()
    assert actual_data == expected_data
