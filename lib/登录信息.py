import os
from configparser import ConfigParser

config = ConfigParser()
ini_path = "data/setting.ini"


def init_ini():
    # 如果文件不存在，创建并初始化 setting.ini
    if not os.path.exists(ini_path):
        os.makedirs(os.path.dirname(ini_path), exist_ok=True)
        config["setting"] = {"token": "", "auto_feed": "true", "auto_extend": "false"}
        with open(ini_path, "w") as configfile:
            config.write(configfile)


def write_value(key, value):
    # 读取配置文件
    config.read(ini_path)
    # 写入新的 token 值
    config.set("setting", key, value)
    # 保存配置文件
    with open(ini_path, "w") as configfile:
        config.write(configfile)


def get_value(key):
    # 读取配置文件
    config.read(ini_path)
    # 返回 token 的值
    return config.get("setting", key)


init_ini()

headers = {
    "User-Agent": "com.caike.union/4.0.2-90585 Dalvik/2.1.0 (Linux; U; Android 14; 2211133C Build/UKQ1.230804.001)",
    "Content-Type": "application/x-www-form-urlencoded",
    "token": get_value("token"),
}
