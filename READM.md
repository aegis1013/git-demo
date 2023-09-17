# 版本檢視
	- git --version

# 建立基本資訊
  	- git config --global user.name "your-name"   ["jeffrey"]
	- git config --global user.email "your-email" ["jeffrey@gmail.com"]

# git 設定資訊
	- git config --list

# 切換目錄 cd
	- cd\
	- cd d:\
	- cd cd C:\Users\USER\Desktop\django\2023-09-17\GIT

# 初始本地倉庫 [需有.git的資料夾否則以下無法執行]
	- git init (初始化)

# 檢視目前狀態
	- git status
		-Untrack (未被控管)

# 加入控管
	- git add <filename> (路徑:objects\e6\檔名被A256編碼)
		-Untracked -> Added (加入)
		-Added -> Modified (修改)
	- 四種狀態
		- U (未追蹤)->A (加入追蹤) ->M (修改後未追蹤)
		- D (被刪除後)
	- 以文字檔為主
	
	- git add. 加入所有檔案進入控管(前提新增.gitignore取消要追蹤檔案)
		- 將所有未加入跟變動一次確認 

# 修改後確認
	-M -> A (git add filename)

# 新增忽略檔案
	- .gitignore (檔案名稱)
	- *.jpg
	- .vscode/
	# * 代表所有檔案名稱
	# 資料夾要帶 .(name)/ 倒斜線 

# 恢復上一動作
	- git checkout .(帶.代表所有檔案 ("檔名"))

# 恢復刪除後檔案
	- git restore <filename>

# 確認刪除後檔案
	- git add . or <filename>

# 查找控管檔案
	- git ls-files
	- git ls-files -s (objects編碼)

# 檢視object內容物
	- git cat-file -t (sha-1六碼)
	- git cat-file -p (sha-1六碼)
	# t (型態(blob)) ,p (內容)

# 正式儲存到倉庫區
	- git commit -m "任意註記message"
		     -am "任意註記message"
	- git commit --amend (合併commit)
		     - vim 
			- i (insert) 
			esc (切換命令列)
			- :wq(寫入離開)
			- q! (不寫入離開)

# 檢視目前有幾個 commit
	- git log
	- q (強制離開)
	- git log --oneline
		- 每個commit(縮成一行檢視)
	
	C:\Users\USER\Desktop\django\2023-09-17\GIT\demo>git log
	commit 4f226cb9c9896bb484d49ec960559e4e4b39b6a8 (HEAD -> master)
	Author: jeffrey <jeffrey@gmail.com>
	Date:   Sun Sep 17 11:43:59 2023 +0800

	    初始環境

#	。 git cat-file -t 4f226c 

	C:\Users\USER\Desktop\django\2023-09-17\GIT\demo>git cat-file -t 4f226c 
	commit

	。 git cat-file -p commit-sha1

	C:\Users\USER\Desktop\django\2023-09-17\GIT\demo>git cat-file -p 4f226c 
	tree a3137cc7ac64a24f380f07577e060fc3cc3923ad
	author jeffrey <jeffrey@gmail.com> 1694922239 +0800
	committer jeffrey <jeffrey@gmail.com> 1694922239 +0800

	初始環境


	。 git cat-file -p tree-sha1

	C:\Users\USER\Desktop\django\2023-09-17\GIT\demo>git cat-file -p a3137c 
	100644 blob 6479b7bfe9d629ae478117283560688b3cad9e17    .gitignore
	100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    1.txt
	100644 blob d8263ee9860594d2806b0dfd1bfd17528b0ba2a4    2.txt
	100644 blob e440e5c842586965a7fb77deda2eca68612b1f53    3.txt
	100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    4.txt
	100644 blob add3e65f9fa2dd75dc9c147bf4c70b451154cb14    test.py

# 直接刪除檔案
	# 檔案在暫存區
		- 完整刪除
		- git rm -f "<filename>"
	# 檔案在倉庫區
		- 刪除
			-git add (確認刪除)
		- 恢復
			- git restore --staged <filename>
				-git add (確認刪除)
				-git restore (恢復)

# 暫存/倉庫區 
	- git rm --cached <filename>
	- 移回工作目錄(不控管)

# 分支 
	- master (預設)
	- git branch 
		-分支列表
	- git branch <branch-name>
		-產生分支

# 切換分支
	- git checkout <branch-name>
		- git checkout -b <branch-name> (新建分支並切換)
	
	- git checkout -commit (sha1) [只會回到過去觀察]
	- git checkout HEAD~[0or1,2,3....] (前幾個分支)

# 合併分支
	- git merge (合併)
	- 切換到 git checkout master
		-git merge <branch-name>
	
	# 合併發生衝突
		- 選擇以哪個分支(current/incoming/both)
		- git merge abort
			- 取消合併

# 刪除分支
	- git branch -D <branch-name>

# 重置指令
	- git reset commit (sha1)
	- git reset --mixed commit(sha1) (同上 為預設值)
	- git reset --soft commit(sha1) #較為少用
	- git reset --hard commit(sha1)
	- git reset --hard HEAD~[0or1,2,3....] (前幾個分支)
	# 反悔 reset
		- git reset ORIG_HEAD

# 查找過往的commit記錄
	- git reflog

#加入遠端倉庫
	- git remote add origin 	
	
	- git remote -v 顯示目前連結的遠端倉庫

	- git push -u origin master  從本地推送到雲端	

#【aegis1013的git_倉庫】
	-echo "# git-demo" >> README.md
	-git init
	-git add README.md
	-git commit -m "first commit"
	-git branch -M main
	-git remote add origin https://github.com/aegis1013/git-demo.git (第一個綁定步驟	)
	-git push -u origin main  (串流)


--------------------------------------------------------------------------------

# VSCode 
	- Terminal 改cmd
	- file -> preferences -> settings 
		- [file.ex]
		- zoom [Mouse Wheel Zoom]
		- format [editor:format on save]
	- ctrl+shift+p
	# 更改Terminal (更改預設終端機)
		- >default [select default profile]
	- cls 
		-清空terminal