from langchain_pdf.exporter import export_pdf


SAMPLE_TEXT = """
## Generative AI with LangChain

### Course Overview
Generative AI is transforming how software is built, scaled, and experienced. This course is designed to help learners move beyond theory and actually **build real-world applications** using LangChain.

Rather than focusing only on APIs or prompts, the course emphasizes **system thinking**—how different components like LLMs, memory, tools, and retrievers work together. By the end of the course, learners will not just “know LangChain”, but understand **why each part exists** and **when to use it**.

---

## Why This Course Exists

Many developers struggle with one common problem:  
they can call an LLM, but they **cannot design a system around it**.

This course was created to close that gap.

It focuses on:
- building reliable pipelines instead of one-off prompts
- reducing hallucinations using retrieval
- structuring prompts for consistency
- thinking like an AI engineer, not a chatbot user

This is especially useful if you want to:
- move into AI/ML roles
- build production-ready AI tools
- create SaaS products powered by LLMs

---

## Target Audience

This course is suitable for learners who already have some technical background and want to **level up practically**.

- Software Developers who want to integrate LLMs into real applications
- Data Scientists interested in applying LLMs beyond notebooks
- AI Enthusiasts exploring modern GenAI frameworks
- Product Managers who want to understand AI capabilities deeply
- Technical Leads designing AI-powered systems

#careers #AIJobs #TechGrowth

---

## Prerequisites

You do NOT need to be an AI researcher to take this course.

However, the following will help:
- Basic Python programming knowledge
- Understanding of APIs and JSON
- Familiarity with how web services work

Optional but helpful:
- Basic ML concepts (classification, embeddings)
- Experience with backend frameworks like FastAPI

If you don’t have these, the course still explains concepts in a **clear and practical way**.

---

## What You Will Learn

By the end of this course, you will be able to:

- Understand how Large Language Models actually work (at a practical level)
- Use LangChain to connect prompts, models, and tools
- Design multi-step chains instead of single prompts
- Build question-answering systems using your own data
- Implement memory to maintain conversational context
- Create simple AI agents that can reason and act
- Think critically about limitations, costs, and ethics of AI systems

#learning #Upskilling #AIWorkflow

---

## Learning Philosophy

This course follows a **build-first philosophy**.

That means:
- less theory, more implementation
- fewer slides, more code
- fewer buzzwords, more clarity

Every concept is introduced with:
1. A clear explanation
2. A real-world example
3. A practical use case
4. A discussion of trade-offs

This ensures long-term understanding instead of short-term memorization.

---

## Final Thought

Generative AI is not magic.  
It is a **tool**.

Those who learn how to structure it, control it, and integrate it properly will stand out in the next wave of software development.

This course is one step in that direction.

#FutureOfWork #AIBuilder #LangChain

"""


if __name__ == "__main__":
    export_pdf(
        text=SAMPLE_TEXT,
        output_path="reports/langchain_course_overview.pdf",
        title="LangChain Course Overview"
    )

    print("✅ PDF generated: reports/langchain_course_overview.pdf")