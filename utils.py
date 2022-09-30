from fastapi.requests import Request


def log(tag="MyApp", message="", request: Request = None):
    with open("log.txt", mode="a+") as fw:
        fw.write(f"{tag}: {message}\n")
        fw.write(f"\t{request.url}\n")
