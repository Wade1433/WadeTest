#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
演示導入其他模組時 __name__ 的行為
"""

print("=== 開始導入 name_main_explanation 模組 ===")

# 導入我們剛才創建的模組
import name_main_explanation

print("=== 導入完成 ===")

# 使用導入模組中的函數
print(f"\n使用導入模組的函數: {name_main_explanation.greet('模組使用者')}")

print(f"當前檔案的 __name__ 是: {__name__}")