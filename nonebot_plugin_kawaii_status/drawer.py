import platform
from io import BytesIO

import cpuinfo
import nonebot
from nonebot import get_plugin_config
from PIL import Image, ImageDraw, ImageFont
from nonebot.config import Config as BotConfig
from nonebot import __version__ as __nb_version__

from .model import get_status_info
from .utils import truncate_string
from . import __version__ as __status_version__
from .path import (
    bg_img_path,
    adlam_font_path,
    baotu_font_path,
    marker_img_path,
    spicy_font_path,
)
from .color import (
    cpu_color,
    ram_color,
    disk_color,
    swap_color,
    details_color,
    nickname_color,
    transparent_color,
)

bot_config = get_plugin_config(BotConfig)

system = platform.uname()
nickname = list(bot_config.nickname)[0] if bot_config.nickname else "unknown"

adlam_fnt = ImageFont.truetype(str(adlam_font_path), 36)
spicy_fnt = ImageFont.truetype(str(spicy_font_path), 38)
baotu_fnt = ImageFont.truetype(str(baotu_font_path), 64)


def draw() -> bytes:
    """绘图"""

    loaded_plugins = nonebot.get_loaded_plugins()

    with Image.open(bg_img_path).convert("RGBA") as base:
        img = Image.new("RGBA", base.size, (0, 0, 0, 0))
        marker = Image.open(marker_img_path)

        cpu, ram, swap, disk = get_status_info()

        cpu_info = f"{cpu.usage}% - {cpu.freq}Ghz [{cpu.core}core]"
        ram_info = f"{ram.usage} / {ram.total} GB"
        swap_info = f"{swap.usage} / {swap.total} GB"
        disk_info = f"{disk.usage} / {disk.total} GB"

        content = ImageDraw.Draw(img)
        content.text((103, 581), nickname, font=baotu_fnt, fill=nickname_color)
        content.text((251, 772), cpu_info, font=spicy_fnt, fill=cpu_color)
        content.text((251, 927), ram_info, font=spicy_fnt, fill=ram_color)
        content.text((251, 1081), swap_info, font=spicy_fnt, fill=swap_color)
        content.text((251, 1235), disk_info, font=spicy_fnt, fill=disk_color)

        content.arc(
            (103, 724, 217, 838),
            start=-90,
            end=(cpu.usage * 3.6),
            width=115,
            fill=cpu_color,
        )
        content.arc(
            (103, 878, 217, 992),
            start=-90,
            end=(ram.usage * 3.6),
            width=115,
            fill=ram_color,
        )
        content.arc(
            (103, 1032, 217, 1146),
            start=-90,
            end=(swap.usage * 3.6),
            width=115,
            fill=swap_color,
        )
        content.arc(
            (103, 1186, 217, 1300),
            start=-90,
            end=(disk.usage * 3.6),
            width=115,
            fill=disk_color,
        )

        content.ellipse((108, 729, 212, 833), width=105, fill=transparent_color)
        content.ellipse((108, 883, 212, 987), width=105, fill=transparent_color)
        content.ellipse((108, 1037, 212, 1141), width=105, fill=transparent_color)
        content.ellipse((108, 1192, 212, 1295), width=105, fill=transparent_color)

        content.text(
            (352, 1378),
            f"{truncate_string(cpuinfo.get_cpu_info()['brand_raw'])}",
            font=adlam_fnt,
            fill=details_color,
        )
        content.text(
            (352, 1431),
            f"{truncate_string(system.system + ' ' + system.release)}",
            font=adlam_fnt,
            fill=details_color,
        )
        content.text(
            (352, 1484),
            f"NoneBot {__nb_version__} x Plugin {__status_version__}",
            font=adlam_fnt,
            fill=details_color,
        )
        content.text(
            (352, 1537),
            f"{len(loaded_plugins)} loaded",
            font=adlam_fnt,
            fill=details_color,
        )

        nickname_length = baotu_fnt.getlength(nickname)
        img.paste(marker, (103 + int(nickname_length) + 44, 595), marker)

        out = Image.alpha_composite(base, img)

        byte_io = BytesIO()
        out.save(byte_io, format="png")
        img_bytes = byte_io.getvalue()

        return img_bytes
