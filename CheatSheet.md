# 開發工具指令速查表 (Cheat Sheet)

紀錄了在 Linux 與 Windows 環境下進行 Git 操作與 C/C++ 編譯的常用指令。

---

## Git 遠端倉庫操作

### 1. 取得專案 (Clone)
* **HTTPS 方式** (初次使用較簡單):

	```bash
	git clone https://github.com/kailiang1228/LeetcodePractice.git
	```

* **SSH 方式** (推薦，需先設定公鑰):

	```bash
	git clone git@github.com:kailiang1228/LeetcodePractice.git
	```

### 2. 日常開發流程

* 同步遠端最新進度

	```bash
	git pull origin main
	```
* 修復連線問題 (HTTPS 轉 SSH)

	```bash
	git remote set-url origin git@github.com:kailiang1228/LeetcodePractice.git
	```

*

* 提交變更

	```bash
	git add .
	git commit -m "feat: 描述你的改動"
	git push origin main
	```

## C/C++ 編譯與執行 (Linux)

### 1. C 語言編譯 (GCC)

* 基本編譯

	```bash
	gcc solution.c -o solution
	```

* 專業開發推薦 (顯示詳細警告與除錯資訊)

	```bash
	gcc solution.c -o solution -Wall -Wextra -g
	```

	* `-Wall`: 顯示所有警告 (Warning All)
	* `-Wextra`: 顯示額外警告
	* `-g`: 加入除錯資訊 (供 GDB 使用)

### 2. C++ 語言編譯 (G++)

* 基本編譯

	```bash
	g++ solution.cpp -o solution_cpp
	```

### 3. 執行程式

```bash
./solution      # 執行 C 程式
./solution_cpp  # 執行 C++ 程式
```

## 📂 多檔案自動化編譯 (Makefile)

當專案檔案變多時，建立 Makefile，範例如下：

```Makefile
# 定義編譯規則 (注意：指令行開頭必須是一個 Tab 鍵，不能是空白)
all:
	gcc solution.c -o solution -Wall -Wextra

# 清理編譯產生的執行檔
clean:
	rm -f solution
```

執行自動編譯：`make`
執行清理工作：`make clean`

## ⚠️ 疑難排解 (Troubleshooting)

* 編譯器路徑報錯：若 VS Code 提示 IntelliSense 錯誤，請檢查 `.vscode/` 是否已被加入 `.gitignore`。
* 無法追蹤已存在的 `.vscode`：若要停止追蹤已上傳的設定檔：

	```bash
	git rm -r --cached .vscode
	git commit -m "chore: stop tracking .vscode"
	git push origin main
	```
