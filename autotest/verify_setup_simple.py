#!/usr/bin/env python
"""验证测试环境是否正常"""
import sys

print("=" * 50)
print("1. 检查Python版本...")
print("   Python版本:", sys.version)

print("\n2. 检查依赖安装...")
try:
    import pytest
    print("   pytest: OK")
except ImportError:
    print("   pytest: 未安装")

try:
    import requests
    print("   requests: OK")
except ImportError:
    print("   requests: 未安装")

try:
    import yaml
    print("   pyyaml: OK")
except ImportError:
    print("   pyyaml: 未安装")

try:
    import allure
    print("   allure: OK")
except ImportError:
    print("   allure: 未安装")

print("\n3. 检查配置文件...")
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config", "env.yaml")
if os.path.exists(config_path):
    print("   配置文件: 存在")
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
        print("   base_url:", config.get("base_url"))
else:
    print("   配置文件: 不存在")

print("\n4. 检查项目结构...")
dirs_to_check = ["api", "core", "testcases", "config"]
for d in dirs_to_check:
    dir_path = os.path.join(current_dir, d)
    if os.path.exists(dir_path):
        print(f"   {d}/: 存在")
    else:
        print(f"   {d}/: 不存在")

print("\n" + "=" * 50)
print("环境验证完成！")
print("\n注意：运行实际测试前请先启动后端服务！")
