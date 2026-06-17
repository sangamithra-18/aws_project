from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
  return {"message": "Hello World!THIS IS A TEST!"
  ""}  

@app.get("/health")
def health():
    return {"status": "healthy"}    


@app.get("/home")
def home():
    return {"message": "CI/CD TEST"}