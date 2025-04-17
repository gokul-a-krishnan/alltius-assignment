from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI

load_dotenv(override=True)
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools import get_insurance_doc, get_angelone_doc
import os

azure_endpoint = os.environ.get("AZURE_OAI_CHAT_ENDPOINT")
azure_deployment = os.environ.get("AZURE_OAI_CHAT_DEPLOYMENT")
api_key = os.environ.get("AZURE_OAI_CHAT_KEY")
api_version = os.environ.get("AZURE_OAI_CHAT_API_VERSION")
memory = MemorySaver()

llm = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    azure_deployment=azure_deployment,
    api_key=api_key,
    api_version=api_version,
)

agent = create_react_agent(
    model=llm,
    tools=[get_insurance_doc, get_angelone_doc],
    checkpointer=memory
)


def chat(query, thread_id=None):
    history = []
    mem = memory.get(config={
        "configurable": {
            "thread_id": 1,
        }
    })
    if mem:
        history = mem["channel_values"]["messages"]
    if len(history) == 0:
        history = [
            SystemMessage(
                content="You are a helpful assistant. Answer the questions as best as you can. use the tools to get the information you need. Do not make up answers. If you do not know the answer, say 'I don't know'."
            )
        ]
    history.append(HumanMessage(query))
    res = agent.invoke({
        "messages": history
    },
        config={
            "configurable": {
                "thread_id": thread_id,
            }
        })

    return res["messages"][-1].content
