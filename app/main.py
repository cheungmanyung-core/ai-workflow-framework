from fastapi import FastAPI

app = FastAPI(title="AI Workflow Automation Framework")

@app.get("/")
def index():
    return {"message": "Welcome to AI Workflow Framework!"}

@app.get("/health")
def health():
    return {"status": "ok"}

# 先占位：后面会替换为真实的AI/Notion集成功能
@app.post("/tasks/summarize")
def summarize(text: str):
    return {"summary": f"Summary of: {text}"}

