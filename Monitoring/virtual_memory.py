import psutil
def get_ram_percent():
    return psutil.virtual_memory().percent