from dataclasses import dataclass

import psutil


@dataclass
class CPUInfo:
    core: int
    """CPU 物理核心数"""
    usage: float
    """CPU 占用"""
    freq: float
    """CPU 的时钟速度（单位：GHz）"""

    @classmethod
    def get_cpu_info(cls):
        cpu_core = psutil.cpu_count(logical=False)
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_freq = round(psutil.cpu_freq().current / 1000, 2)

        return CPUInfo(core=cpu_core, usage=cpu_usage, freq=cpu_freq)


@dataclass
class RAMInfo:
    """RAM 信息（单位：GB）"""

    total: float
    """RAM 总量"""
    usage: float
    """当前 RAM 占用"""

    @classmethod
    def get_ram_info(cls):
        ram_total = round(psutil.virtual_memory().total / (1024**3), 2)
        ram_usage = round(psutil.virtual_memory().used / (1024**3), 2)

        return RAMInfo(total=ram_total, usage=ram_usage)


@dataclass
class SwapMemory:
    """Swap 信息（单位：GB）"""

    total: float
    """Swap 总量"""
    usage: float
    """当前 Swap 占用"""

    @classmethod
    def get_swap_info(cls):
        swap_total = round(psutil.swap_memory().total / (1024**3), 2)
        swap_usage = round(psutil.swap_memory().used / (1024**3), 2)

        return SwapMemory(total=swap_total, usage=swap_usage)


@dataclass
class DiskInfo:
    """硬盘信息"""

    total: float
    """硬盘总量"""
    usage: float
    """当前硬盘占用"""

    @classmethod
    def get_disk_info(cls):
        disk_total = round(psutil.disk_usage("/").total / (1024**3), 2)
        disk_usage = round(psutil.disk_usage("/").used / (1024**3), 2)

        return DiskInfo(total=disk_total, usage=disk_usage)


def get_status_info() -> tuple[CPUInfo, RAMInfo, SwapMemory, DiskInfo]:
    """获取 `CPU` `RAM` `SWAP` `DISK` 信息"""
    cpu_info = CPUInfo.get_cpu_info()
    ram_info = RAMInfo.get_ram_info()
    swap_info = SwapMemory.get_swap_info()
    disk_info = DiskInfo.get_disk_info()

    return cpu_info, ram_info, swap_info, disk_info
