# Fast-API

A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

> **Note:** This project is for learning purposes. It demonstrates basic web functionalities such as uploading blogs, creating users, and more.

## Features

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI and JSON Schema.

## Installation

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

## Usage

Start the server with:

```bash
uvicorn main:app --reload
```

Replace `main` with the name of your Python file (without the `.py` extension).

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## API Endpoints

| Method | Endpoint      | Description         |
|--------|--------------|---------------------|
| GET    | `/`          | Root endpoint       |
| POST   | `/blogs`     | Upload a new blog   |
| POST   | `/users`     | Create a new user   |
| ...    | ...          | ...                 |

_Add your endpoints and descriptions here._

## Documentation

Once the server is running, access:

- Interactive API docs (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Alternative API docs (ReDoc): [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

This project is licensed under the MIT License.
