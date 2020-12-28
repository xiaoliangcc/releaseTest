# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypePinMatrixRequestType = Literal[1, 2, 3, 4, 5, 6, 7]
    except ImportError:
        pass


class PinMatrixRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 18

    def __init__(
        self,
        type: EnumTypePinMatrixRequestType = None,
    ) -> None:
        self.type = type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('type', p.EnumType("PinMatrixRequestType", (1, 2, 3, 4, 5, 6, 7)), 0),
        }