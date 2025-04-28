from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

def generate_cover_letter(resume_text, job_description, model="gpt-4o"):
    llm = ChatOpenAI(model_name=model)
    prompt = ChatPromptTemplate.from_template(
        "Given the resume:\n{resume}\n\nAnd job description:\n{job}\n\nWrite a personalized cover letter."
    )
    chain = prompt | llm
    response = chain.invoke({"resume": resume_text, "job": job_description})
    return response.content
    
    return response.content.strip()  # Return the generated cover letter content    