# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeSafetyCheckLevel = Literal[0, 1]
    except ImportError:
        pass


class ApplySettings(p.MessageType):
    MESSAGE_WIRE_TYPE = 25

    def __init__(
        self,
        language: str = None,
        label: str = None,
        use_passphrase: bool = None,
        homescreen: bytes = None,
        auto_lock_delay_ms: int = None,
        display_rotation: int = None,
        passphrase_always_on_device: bool = None,
        safety_checks: EnumTypeSafetyCheckLevel = None,
        use_ble: bool = None,
        use_se: bool = None,
        is_bixinapp: bool = None,
        fastpay_pin: bool = None,
        fastpay_confirm: bool = None,
        fastpay_money_limit: int = None,
        fastpay_times: int = None,
    ) -> None:
        self.language = language
        self.label = label
        self.use_passphrase = use_passphrase
        self.homescreen = homescreen
        self.auto_lock_delay_ms = auto_lock_delay_ms
        self.display_rotation = display_rotation
        self.passphrase_always_on_device = passphrase_always_on_device
        self.safety_checks = safety_checks
        self.use_ble = use_ble
        self.use_se = use_se
        self.is_bixinapp = is_bixinapp
        self.fastpay_pin = fastpay_pin
        self.fastpay_confirm = fastpay_confirm
        self.fastpay_money_limit = fastpay_money_limit
        self.fastpay_times = fastpay_times

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('language', p.UnicodeType, 0),
            2: ('label', p.UnicodeType, 0),
            3: ('use_passphrase', p.BoolType, 0),
            4: ('homescreen', p.BytesType, 0),
            6: ('auto_lock_delay_ms', p.UVarintType, 0),
            7: ('display_rotation', p.UVarintType, 0),
            8: ('passphrase_always_on_device', p.BoolType, 0),
            9: ('safety_checks', p.EnumType("SafetyCheckLevel", (0, 1)), 0),
            100: ('use_ble', p.BoolType, 0),
            101: ('use_se', p.BoolType, 0),
            102: ('is_bixinapp', p.BoolType, 0),
            103: ('fastpay_pin', p.BoolType, 0),
            104: ('fastpay_confirm', p.BoolType, 0),
            105: ('fastpay_money_limit', p.UVarintType, 0),
            106: ('fastpay_times', p.UVarintType, 0),
        }