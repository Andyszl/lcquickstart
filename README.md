# LangChain 快速入门与实战项目

## 项目概述
本项目是一个全面的 LangChain 学习与实践平台，涵盖了从基础入门到高级应用的完整学习路径。项目包含多个 Jupyter Notebook 教程、Python 实战脚本，以及基于 Streamlit 的交互式 Web 应用，旨在帮助开发者快速掌握 LangChain、LangGraph 及相关 AI/Agent 技术。

## 🎯 学习目标
- 掌握 LangChain 核心概念和基础用法
- 学习构建智能 Agent 和自动化工具
- 实践 RAG（检索增强生成）系统开发
- 探索 LangGraph 工作流编排
- 了解 AI 数据分析和可视化

## 📁 项目结构

### LangChain 基础教程 (`langchian/`)
1. **`1、quickstart.ipynb`** - LangChain 快速入门
   - DeepSeek API 集成与调用
   - LangChain 模型初始化与基础对话
   - 环境配置与依赖管理

2. **`2、LCEL及完善.ipynb`** - LCEL（LangChain Expression Language）深入学习
   - 链式调用与表达式语法
   - 复杂工作流构建
   - 错误处理与优化技巧

3. **`3、tools.ipynb`** - 工具开发与集成
   - 自定义工具创建
   - 工具调用与参数处理
   - 工具链组合应用

4. **`4、简单agent爬虫.py`** - 基础 Agent 爬虫
   - PlayWright 浏览器自动化
   - 简单网页内容抓取
   - Agent 任务执行与错误处理

5. **`5、复杂agent.py`** - 高级 Agent 应用
   - 网站内容智能总结
   - PDF 报告自动生成
   - 串行链与优化链设计模式
   - 中文支持与格式化输出

6. **`6、rag.ipynb` & `6、rag.py`** - RAG 系统实现
   - PDF 文档处理与向量化
   - FAISS 向量数据库构建
   - 基于文档的智能问答
   - Streamlit Web 界面开发

7. **`7、AI_data.py`** - AI 数据分析
   - 数据可视化与图表生成
   - AI 辅助数据分析
   - 自动化报告生成

### LangGraph 工作流 (`langgraph/`)
1. **`1、入门演示.ipynb`** - LangGraph 基础概念
   - 图结构设计与节点定义
   - 状态管理与工作流控制
   - 天气查询 Agent 实战

2. **`2、langgraph图理论学习.ipynb`** - 图理论深入
   - 复杂工作流设计模式
   - 条件分支与循环处理
   - 状态持久化与恢复

3. **`3、langgraph实战入门演示.ipynb`** - 实战项目
   - 多步骤任务编排
   - 工具集成与调用
   - 实际业务场景应用

### LangChain 1.0 新特性 (`LangChain1.0/`)
- **`agent开发.ipynb`** - LangChain 1.0 Agent 开发
  - 新版本特性介绍
  - create_agent 抽象使用
  - 中间件模式与扩展开发

### 数据与输出 (`data/`)
- **`titanic.csv`** - 示例数据集
- **`LangChain入门.pdf`** - 学习资料
- **`results/`** - 输出结果目录
  - 生成的 PDF 报告
  - 数据分析图表
  - 网站摘要结果

### 向量数据库 (`faiss_db/`)
- FAISS 索引文件
- 向量存储与检索数据

## 🔧 环境配置

### 系统要求
- Python 3.8+
- Windows/Linux/macOS

### 核心依赖
```bash
pip install langchain langchain-community langchain-openai
pip install deepseek-langchain langchain-deepseek
pip install streamlit gradio
pip install playwright pandas numpy
pip install faiss-cpu PyPDF2 reportlab
pip install python-dotenv jupyter
```

### API 密钥配置
项目使用 `.env` 文件管理 API 密钥，支持以下服务：
- **DeepSeek API** - 主要语言模型
- **OpenAI API** - 嵌入模型和 GPT 系列
- **Tavily API** - 网络搜索服务
- **OpenWeather API** - 天气查询服务

## 🚀 快速开始

### 1. 环境准备
```bash
# 克隆项目
git clone <项目地址>
cd lcquickstart

# 安装依赖
pip install -r requirements.txt

# 配置 API 密钥
cp .env.example .env
# 编辑 .env 文件，填入你的 API 密钥
```

### 2. 运行示例
```bash
# 启动 Jupyter Notebook
jupyter notebook

# 运行 Streamlit RAG 应用
streamlit run langchian/6、rag.py

# 运行复杂 Agent
python langchian/5、复杂agent.py
```

### 3. 学习路径建议
1. **基础入门** → 先学习 `1、quickstart.ipynb`
2. **工具开发** → 掌握 `3、tools.ipynb`
3. **Agent 开发** → 实践 `4、简单agent爬虫.py`
4. **高级应用** → 挑战 `5、复杂agent.py`
5. **RAG 系统** → 体验 `6、rag.py` Web 应用
6. **工作流编排** → 学习 LangGraph 系列

## 💡 核心特性

### 🤖 智能 Agent
- 支持多种模型（DeepSeek、OpenAI）
- 浏览器自动化与网页抓取
- 多步骤任务执行与错误处理
- 工具集成与扩展

### 📚 RAG 系统
- PDF 文档智能处理
- 向量数据库构建与检索
- 基于文档的问答系统
- Web 界面交互体验

### 📊 数据可视化
- AI 辅助数据分析
- 自动化图表生成
- PDF 报告导出
- 中文内容支持

### 🔄 工作流编排
- LangGraph 图结构工作流
- 状态管理与持久化
- 条件分支与循环控制
- 复杂业务逻辑实现

## 🔍 实际应用场景

### 内容处理
- 网站内容智能总结
- 文档批量处理与分析
- 多语言内容生成
- PDF 报告自动化生成

### 数据分析
- 业务数据智能分析
- 趋势预测与洞察
- 可视化图表生成
- 交互式仪表板

### 自动化办公
- 智能客服系统
- 邮件自动处理
- 文档分类与归档
- 工作流程自动化

## 📚 学习资源

### 官方文档
- [LangChain 官方文档](https://python.langchain.com/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [DeepSeek API 文档](https://platform.deepseek.com/)
- [OpenAI API 文档](https://platform.openai.com/docs)

### 社区资源
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [Streamlit 文档](https://docs.streamlit.io/)

## ⚠️ 注意事项

### API 使用
- 妥善保管 API 密钥，不要提交到代码仓库
- 注意 API 调用频率限制和费用
- 建议使用测试环境进行开发

### 依赖管理
- 定期更新依赖包以获得最新功能
- 注意不同包版本之间的兼容性
- 使用虚拟环境隔离项目依赖

### 性能优化
- 大文件处理时注意内存使用
- 合理设置超时时间和重试机制
- 考虑使用缓存提高响应速度

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进项目！

### 提交规范
- 清晰的提交信息描述
- 适当的代码注释和文档
- 测试通过后再提交

### 开发建议
- 遵循 Python 编码规范
- 添加必要的错误处理
- 考虑代码的可扩展性

## 📞 联系方式

如有问题或建议，欢迎通过以下方式联系：
- 提交 GitHub Issue
- 发送邮件反馈
- 参与社区讨论

---

**Happy Coding! 🎉**

希望这个项目能帮助你快速掌握 LangChain 技术栈，构建出强大的 AI 应用！
