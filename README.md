# 待辦事項應用程式

## 專案描述

這是一個簡單的待辦事項（To-Do List）應用程式，使用 **Python** 和 **PySimpleGUI** 製作，用於管理日常待辦事項。程式會將所有的待辦事項記錄到檔案 `todos_list.txt` 中，方便儲存和載入。

### 功能

- **新增待辦事項**：用戶可以輸入新待辦事項並加入到清單中。
- **修改待辦事項**：選取現有待辦事項，進行內容修改並保存。
- **刪除待辦事項**：選取不需要的待辦事項並將其從清單中移除。
- **資料保存**：所有的待辦事項會自動保存到 `todos_list.txt` 文件，避免資料丟失。

## 使用技術

- **Python**：核心程式語言。
- **PySimpleGUI**：建立簡單且直觀的使用者圖形介面（GUI）。
- **文本檔案（todos_list.txt）**：用於讀取與儲存待辦事項。

## 程式結構

### 主要檔案

1. **`gui.py`**  
   程式的主要邏輯，包括：
   - 建立 GUI 介面。
   - 處理新增、修改、刪除待辦事項的功能。
   - 調用 `function.py` 與檔案 `todos_list.txt` 進行讀寫操作。

2. **`function.py`**  
   模組化程式邏輯，專門負責讀取與寫入待辦事項清單。包含以下函數：
   - `get_todo()`：讀取 `todos_list.txt` 的內容，返回待辦事項列表。
   - `write_todos(todos_word)`：將待辦事項列表寫入到 `todos_list.txt`。

3. **`todos_list.txt`**  
   存儲所有待辦事項的文本檔案。程式啟動時會讀取此檔案，並在關閉時更新內容。

## 使用方法

### 準備環境

1. 安裝 Python 3.x。
2. 安裝所需模組：

   ```bash
   pip install PySimpleGUI
