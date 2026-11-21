# 待办清单（Streamlit 练手项目）

一个用 Python + Streamlit 做的网页版待办清单，适合刚入门网页应用时练手。

## 功能

- 添加任务
- 勾选标记完成 / 取消完成
- 删除任务
- 任务数据保存在本地 `data/todos.json`，刷新页面不丢失
- 顶部显示任务总数、已完成数、待完成数

## 本地运行

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

浏览器会自动打开 `http://localhost:8501`。

## 项目结构

```
streamlit-todo/
├── app.py              # 主程序，所有逻辑都在这里
├── requirements.txt    # 依赖清单
├── .gitignore          # 忽略虚拟环境和运行数据
└── data/todos.json     # 运行后自动生成，保存任务
```

## 下一步

可以试着加这些功能练手：

- 按完成状态筛选任务
- 给任务加优先级
- 修改任务文字
- 用 GitHub Copilot 帮你写其中某个功能，对比它给的代码和你想的有何不同
