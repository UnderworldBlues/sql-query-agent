from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_google_genai import ChatGoogleGenerativeAI  
from postgres_connection import db, api_key

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
toolkit = SQLDatabaseToolkit(db=db, llm=model)
tools = toolkit.get_tools()