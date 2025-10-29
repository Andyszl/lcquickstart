from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_sync_playwright_browser
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv 
load_dotenv(override=True)


DeepSeek_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# print(DeepSeek_API_KEY)  # 可以通过打印查看

# 初始化 Playwright 浏览器：
# 使用默认参数，create_sync_playwright_browser不支持slow_mo参数
sync_browser = create_sync_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=sync_browser)
tools = toolkit.get_tools()

# 通过 LangChain Hub 拉取提示词模版
prompt = hub.pull("hwchase17/openai-tools-agent")

# # 初始化模型
model = init_chat_model("deepseek-chat", model_provider="deepseek")

# 通过 LangChain 创建 OpenAI 工具代理
agent = create_openai_tools_agent(model, tools, prompt)

# 通过 AgentExecutor 执行代理
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


if __name__ == "__main__":
    try:
        # 定义任务
        command = {
            "input": "访问这个网站 https://edu.csdn.net/course/detail/38965 并帮我总结一下这个网站的内容"
        }

        # 执行任务，添加错误处理
        print("开始执行任务...")
        response = agent_executor.invoke(command, timeout=60)
        print("任务执行成功！")
        print(response)
    except TimeoutError as e:
        print(f"访问超时错误: {e}")
        print("建议：检查网络连接或尝试访问其他网站")
    except Exception as e:
        print(f"执行过程中发生错误: {e}")
    finally:
        # 确保浏览器正确关闭
        if 'sync_browser' in locals():
            sync_browser.close()
            print("浏览器已关闭")