from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
  return {"message": "Hello World!THIS IS A TEST! and cicd test is working fine"""}  

@app.get("/health")
def health():
    return {"status": "Healthy Healthy"}    


@app.get("/home")
def home():
    return {"message": "CI/CD TEST"}