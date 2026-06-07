# 🧠 AI 心理健康助手 (AI Mental Health Assistant)


## 📖 项目简介

**AI 心理健康助手**是一款面向大众的心理健康服务平台，结合 **AI 大模型技术**，为用户提供 24 小时在线的智能心理咨询、情绪管理、健康知识普及等服务。

项目采用前后端分离架构，包含 **前台用户端** 和 **后台管理端** 两大模块，支持多角色权限隔离与实时流式交互。


## ✨ 核心功能

### 🎨 前台用户端
| 功能模块 | 功能描述 |
| :--- | :--- |
| 👤 **用户注册与登录** | 支持注册新账号或登录已有账号，安全验证机制 |
| 💬 **智能心理咨询** | 基于 AI 大模型进行**实时互动对话**，获取专业的心理疏导与建议 |
| 📔 **情绪日记** | 记录每日情绪变化，平台根据记录数据智能生成**情绪管理建议** |
| 📚 **心理健康知识库** | 检索相关心理健康知识，了解最新的心理理论与治疗方法 |

### 🛠️ 后台管理端
| 功能模块 | 功能描述 |
| :--- | :--- |
| 📊 **数据看板** | 可视化展示运行数据（用户注册量、咨询量、情绪日记记录等） |
| 📝 **文章管理** | 发布、编辑、删除平台文章，动态更新心理健康知识库内容 |
| 📞 **会话管理** | 查看咨询会话列表、用户详细信息及会话历史记录 |
| 🔐 **权限控制** | 基于用户角色（User/Admin）分配不同权限，确保平台数据安全 |

## 自动化测试

基于 pytest + requests 的 API 自动化测试框架

### 安装依赖

```
快速启动
安装依赖 
```bash
npm install
```
运行项目
```bash
npm run dev
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行指定测试文件
pytest testcases/test_user.py

# 生成 Allure 报告
pytest --alluredir=./allure-results
allure serve ./allure-results
```

### 目录结构

```
autotest/
├── api/              # API 接口封装
├── config/           # 配置文件
├── core/             # 核心模块（http请求、日志、断言）
├── testcases/        # 测试用例
├── testdata/         # 测试数据
├── conftest.py       # pytest 配置
├── pytest.ini        # pytest 配置文件
└── requirements.txt  # 依赖
```

## 🛠️ 技术栈

```yaml
核心框架:
  - Vue 3 (Composition API + Script Setup)
  - Vite (极速构建 + 热更新)

UI/样式:
  - Element Plus (企业级组件库)
  - SCSS (CSS 预处理器)

路由与状态:
  - Vue Router 4 (动态路由配置)
  - Pinia (轻量级状态管理)

工具与网络:
  - Axios (HTTP 请求封装与拦截器)
  - ECharts 5 (数据可视化图表)
  - Day.js (时间格式化工具)








