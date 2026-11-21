@echo off
chcp 65001 >nul
cd /d D:\streamlit-todo
echo ============================================
echo   正在把代码推送到 GitHub
echo   接下来可能会弹出窗口让你登录 GitHub
echo   请用浏览器登录你的 122zts 账号并授权
echo ============================================
echo.
git push -u origin main
echo.
echo ============================================
echo   推送结束，如果上面没有红色报错就成功了
echo   现在回到 GitHub 网页刷新一下，应该能看到文件了
echo ============================================
pause
