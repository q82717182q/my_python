strings = ['Apple', 'Banana', 'Cat']
#
# if __name__ == '__main__':
#     for index, string in strings:   # 這種迭代要用enumerate 函式
#         print(f"Index {index} : {string}")
#
#
#
# 在你的程式碼中，出現了一個錯誤，這是因為在 Python 的 for 迴圈中，當你使用 for index, string in strings: 的方式時，Python 預期 strings 是一個可迭代對象（例如列表或元組），並且每個元素本身應該是一個可解包的對象，通常是一個包含兩個元素的元組或列表。
#
# 在你的程式碼中，strings 是一個包含三個字串的列表，而在 for 迴圈中，Python 嘗試將列表中的每個字串視為一個元組 (index, string)，這樣做會導致運行時錯誤。
#
# 修正這個問題的方式是使用 enumerate() 函式來獲取索引和值，就像下面這樣：
#
# python
# 複製程式碼

if __name__ == '__main__':
    for index, string in enumerate(strings):
        print(f"Index {index} : {string}")

# 這樣就會正確地遍歷 strings 列表，並輸出每個元素的索引和值。enumerate() 函式會返回一個可迭代對象，其中每個元素是一個 (index, value) 的元組，這樣就可以在 for 迴圈中同時獲取索引和對應的值了。