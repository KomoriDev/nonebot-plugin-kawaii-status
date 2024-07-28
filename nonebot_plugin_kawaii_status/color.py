from typing import Literal
from typing_extensions import TypeAlias

Color: TypeAlias = Literal[
    "cpu", "ram", "swap", "disk", "nickname", "details", "transparent"
]

cpu_color: tuple[int, int, int, int] = (84, 173, 255, 255)
ram_color: tuple[int, int, int, int] = (255, 179, 204, 255)
swap_color: tuple[int, int, int, int] = (251, 170, 147, 255)
disk_color: tuple[int, int, int, int] = (184, 170, 159, 255)
transparent_color: tuple[int, int, int, int] = (0, 0, 0, 0)
details_color: tuple[int, int, int, int] = (184, 170, 159, 255)
nickname_color: tuple[int, int, int, int] = (84, 173, 255, 255)


def get_color(color: Color) -> tuple[int, int, int, int]:
    return globals()[f"{color}_color"]
