from agent_toolkit import tools, model
from langchain.agents import create_agent

agent = create_agent(model=model, tools=tools)

print("ask a question about the database:")
question = input()
for msg, metadata in agent.stream(
    {"messages": [{"role": "user", "content": question}]}, 
    stream_mode="messages"
):
    msg.pretty_print()