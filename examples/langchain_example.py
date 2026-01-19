from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from langchain_pdf.exporter import export_pdf
from dotenv import load_dotenv

load_dotenv()

PROMPT = """
You are an expert technical educator.

Write a detailed course overview document on the topic below.

Rules:
- Use clear section headings
- Use bullet points where appropriate
- Avoid emojis
- Avoid code blocks
- Do not use markdown formatting like ** or *

Topic:
{topic}
"""


def generate_course_text(topic: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", 
                                   temperature=1.0,
                                )

    prompt = PromptTemplate(
        input_variables=["topic"],
        template=PROMPT
    )

    chain = prompt | llm

    response = chain.invoke({"topic": topic})

    return response.content


if __name__ == "__main__":
    topic = "Generative AI with LangGraph"

    print("🔹 Generating content using LangChain...")
    raw_text = generate_course_text(topic)

    print("🔹 Creating PDF...")
    export_pdf(
        text=raw_text,
        output_path="reports/langgraph_output.pdf",
        title="LangGraph Course Overview"
    )

    print("✅ PDF generated: reports/langgraph_output.pdf")
