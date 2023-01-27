import requests as rq


def test():
    result = rq.post("http://127.0.0.1:8000/user", json={
        "username": "string",
        "email": "user@example.com",
        "full_name": "string",
        "password": "string"
    })
    print(f"==[result: {result.json()}]")


if __name__ == "__main__":
    test()
