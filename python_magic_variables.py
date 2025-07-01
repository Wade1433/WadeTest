#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
展示Python中的各種魔術變數和內建屬性
"""

import os
import sys

def example_function(param1, param2="default"):
    """
    這是一個示例函數
    用來展示函數相關的魔術屬性
    """
    print(f"函數名稱: {example_function.__name__}")
    print(f"函數文檔: {example_function.__doc__}")
    print(f"函數參數: {example_function.__code__.co_varnames}")
    return param1 + str(param2)

class ExampleClass:
    """這是一個示例類別"""
    
    def __init__(self, name):
        self.name = name
    
    def method_example(self):
        """示例方法"""
        return f"Hello from {self.name}"

def main():
    print("=== Python 魔術變數和內建屬性展示 ===\n")
    
    # 1. 模組相關的魔術變數
    print("1. 模組相關的魔術變數:")
    print(f"   __name__: {__name__}")
    print(f"   __file__: {__file__}")
    print(f"   __package__: {__package__}")
    print(f"   __doc__: {__doc__}")
    print()
    
    # 2. 檔案和路徑相關
    print("2. 檔案和路徑相關:")
    print(f"   當前檔案的絕對路徑: {os.path.abspath(__file__)}")
    print(f"   當前檔案所在目錄: {os.path.dirname(__file__)}")
    print(f"   當前工作目錄: {os.getcwd()}")
    print()
    
    # 3. 系統相關
    print("3. 系統相關:")
    print(f"   Python版本: {sys.version}")
    print(f"   平台: {sys.platform}")
    print(f"   Python路徑: {sys.executable}")
    print()
    
    # 4. 函數相關的魔術屬性
    print("4. 函數相關的魔術屬性:")
    example_function("Hello", 123)
    print()
    
    # 5. 類別相關的魔術屬性
    print("5. 類別相關的魔術屬性:")
    print(f"   類別名稱: {ExampleClass.__name__}")
    print(f"   類別文檔: {ExampleClass.__doc__}")
    print(f"   類別模組: {ExampleClass.__module__}")
    print(f"   類別基底類別: {ExampleClass.__bases__}")
    print()
    
    # 6. 物件實例相關
    print("6. 物件實例相關:")
    obj = ExampleClass("測試物件")
    print(f"   物件的類別: {obj.__class__}")
    print(f"   物件的類別名稱: {obj.__class__.__name__}")
    print(f"   物件的字典: {obj.__dict__}")
    print()
    
    # 7. 其他常用的內建變數
    print("7. 其他常用的內建變數:")
    print(f"   __builtins__類型: {type(__builtins__)}")
    print(f"   __cached__ (編譯後的檔案): {__cached__}")
    print()
    
    # 8. 動態獲取屬性
    print("8. 動態獲取屬性示例:")
    print(f"   使用 getattr 獲取物件屬性: {getattr(obj, 'name', '找不到')}")
    print(f"   使用 hasattr 檢查屬性: {hasattr(obj, 'name')}")
    print(f"   使用 dir 列出所有屬性: {len(dir(obj))} 個屬性")

if __name__ == "__main__":
    main()