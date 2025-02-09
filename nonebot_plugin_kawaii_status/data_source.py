from datetime import datetime

from nonebot import get_driver

CURRENT_TIMEZONE = datetime.now().astimezone().tzinfo

driver = get_driver()

_nonebot_run_time: datetime


@driver.on_startup
async def _():
    global _nonebot_run_time
    _nonebot_run_time = datetime.now(CURRENT_TIMEZONE)


def get_nonebot_run_time() -> datetime:
    """获取 Bot 运行时间点"""
    try:
        return _nonebot_run_time
    except NameError:
        raise RuntimeError("NoneBot not running!") from None


def get_bot_uptime() -> int:
    """获取 Bot 运行时长"""
    start_time = get_nonebot_run_time()
    current_time = datetime.now(CURRENT_TIMEZONE)
    delta = current_time - start_time

    return int(delta.total_seconds())


def format_uptime(total_seconds: int) -> str:
    """将 Bot 运行时长转换为可读形式"""
    hours = total_seconds // 3600
    if hours >= 24:
        days, remaining_hours = divmod(hours, 24)
        return f"已运行 {days} 天 {remaining_hours} 小时"
    else:
        minutes = (total_seconds % 3600) // 60
        return f"已运行 {hours} 时 {minutes} 分"
