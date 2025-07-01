#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
演示 if __name__ == "__main__" 的用法
"""

print(f"這個模組的 __name__ 是: {__name__}")

def greet(name):
    """問候函數"""
    return f"你好, {name}!"

def main():
    """主函數"""
    print("這是在 main() 函數中執行的程式碼")
    print(greet("Python學習者"))

# 這裡是關鍵部分
if __name__ == "__main__":
    print("\n--- 這個檔案是直接執行的 ---")
    main()
else:
    print("\n--- 這個檔案是被其他程式導入的 ---")