# numbers = range(6)
# for i in numbers:
#     print(i)


from fastapi import FastAPI

app = FastAPI(
    title="Saturday Class",
    version="0.0.1",
    description="This is a simple API for Saturday class"
)

@app.get("/")
def main():
    return "Hello class"
