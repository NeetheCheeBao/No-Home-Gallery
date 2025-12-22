# No-Home-Gallery

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows-win.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

基于 Python 编写的轻量级工具，用于隐藏资源管理器侧边栏（导航窗格）中烦人的**主文件夹**和**图库**。

## 📸 工具截图
<img src="/IMG/1.png" />

## ✨ 效果展示
|隐藏前|隐藏后|
|---|---|
|<img src="/IMG/2.png" />|<img src="/IMG/3.png" />|

## ⚙️ 原理说明

通过修改 Windows 注册表来实现图标的隐藏与显示。具体修改路径如下：

* **路径**：`HKEY_CURRENT_USER\Software\Classes\CLSID\{GUID}`

**涉及的 GUID：**
* **主文件夹 (Home)**: `{f874310e-b6b7-47dc-bc84-b9e6b38f5903}`
* **图库 (Gallery)**: `{e88865ea-0e1c-4e20-9aa6-edcd0212c87c}`

## ⬇️ 下载使用

前往 [Releases](https://github.com/NeetheCheeBao/No-Home-Gallery/releases)页面下载

## ⚖️ 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。
