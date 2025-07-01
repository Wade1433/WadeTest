#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
展示Python中的魔術方法（Magic Methods / Dunder Methods）
"""

class Person:
    """示範各種魔術方法的類別"""
    
    def __init__(self, name, age):
        """建構子"""
        self.name = name
        self.age = age
        print(f"__init__: 創建了 {name}")
    
    def __str__(self):
        """字串表示（給使用者看的）"""
        return f"Person(姓名: {self.name}, 年齡: {self.age})"
    
    def __repr__(self):
        """字串表示（給開發者看的）"""
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):
        """定義 len() 函數的行為"""
        return len(self.name)
    
    def __eq__(self, other):
        """定義 == 運算子的行為"""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __lt__(self, other):
        """定義 < 運算子的行為"""
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented
    
    def __add__(self, other):
        """定義 + 運算子的行為"""
        if isinstance(other, Person):
            return f"{self.name} 和 {other.name}"
        return NotImplemented
    
    def __getitem__(self, key):
        """定義索引存取的行為"""
        if key == 0:
            return self.name
        elif key == 1:
            return self.age
        else:
            raise IndexError("索引超出範圍")
    
    def __call__(self):
        """讓物件可以像函數一樣被呼叫"""
        return f"{self.name} 說：你好！"
    
    def __del__(self):
        """解構子（物件被刪除時呼叫）"""
        print(f"__del__: {self.name} 被刪除了")

class MathVector:
    """展示數學運算相關的魔術方法"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """向量加法"""
        return MathVector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """向量減法"""
        return MathVector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """純量乘法"""
        return MathVector(self.x * scalar, self.y * scalar)
    
    def __abs__(self):
        """向量長度"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

def main():
    print("=== Python 魔術方法展示 ===\n")
    
    # 1. 基本魔術方法
    print("1. 基本魔術方法:")
    person1 = Person("小明", 25)
    person2 = Person("小華", 30)
    
    print(f"   str(person1): {str(person1)}")
    print(f"   repr(person1): {repr(person1)}")
    print(f"   len(person1): {len(person1)}")
    print()
    
    # 2. 比較運算子
    print("2. 比較運算子:")
    print(f"   person1 == person2: {person1 == person2}")
    print(f"   person1 < person2: {person1 < person2}")
    print()
    
    # 3. 算術運算子
    print("3. 算術運算子:")
    print(f"   person1 + person2: {person1 + person2}")
    print()
    
    # 4. 索引存取
    print("4. 索引存取:")
    print(f"   person1[0]: {person1[0]}")
    print(f"   person1[1]: {person1[1]}")
    print()
    
    # 5. 可呼叫物件
    print("5. 可呼叫物件:")
    print(f"   person1(): {person1()}")
    print()
    
    # 6. 數學向量示例
    print("6. 數學向量示例:")
    v1 = MathVector(3, 4)
    v2 = MathVector(1, 2)
    
    print(f"   v1: {v1}")
    print(f"   v2: {v2}")
    print(f"   v1 + v2: {v1 + v2}")
    print(f"   v1 - v2: {v1 - v2}")
    print(f"   v1 * 2: {v1 * 2}")
    print(f"   abs(v1): {abs(v1)}")
    print()
    
    # 7. 其他有用的魔術方法
    print("7. 其他常用魔術方法:")
    print("   __enter__ 和 __exit__: 用於 with 語句")
    print("   __iter__ 和 __next__: 用於迭代")
    print("   __contains__: 用於 in 運算子")
    print("   __hash__: 用於雜湊表")
    print("   __bool__: 用於布林轉換")

if __name__ == "__main__":
    main()