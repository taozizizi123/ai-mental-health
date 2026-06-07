#!/usr/bin/env python
"""验证测试环境是否正常"""
import sys

print("=" * 50)
print("1. 检查Python版本...")
print(f"   Python版本: {sys.version}")
print("   ✅ Python正常")

print("\n2. 检查依赖安装...")
try:
    import pytest
    print(f"   pytest版本: {pytest.__version__}")
except ImportError:
    print("   ❌ pytest未安装")

try:
    import requests
    print(f"   requests版本: {requests.__version__}")
except ImportError:
    print("   ❌ requests未安装")

try:
    import yaml
    print(f"   pyyaml版本: {yaml.__version__}")
except ImportError:
    print("   ❌ pyyaml未安装")

try:
    import allure
    print(f"   allure正常导入")
except ImportError:
    print("   ❌ allure-pytest未安装")

print("\n3. 检查配置文件...")
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config", "env.yaml")
if os.path.exists(config_path):
    print(f"   ✅ 配置文件存在: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
        print(f"   base_url: {config.get('base_url')}")
else:
    print(f"   ❌ 配置文件不存在: {config_path}")

print("\n4. 检查项目结构...")
dirs_to_check = ["api", "core", "testcases", "config"]
for d in dirs_to_check:
    dir_path = os.path.join(current_dir, d)
    if os.path.exists(dir_path):
        print(f"   ✅ {d}/ 目录存在")
    else:
        print(f"   ❌ {d}/ 目录不存在")

print("\n" + "=" * 50)
print("✅ 环境验证完成！")
print("\n注意：运行实际测试前请先启动后端服务！")
