from random import randint
from sys import argv
from time import sleep, time

from requests import get

MAX_WORD_LENGTH = 0
VERBOSE = True


def wait(minimum: int = 5, maximum: int = 8) -> None:
    random_number = randint(minimum, maximum)
    if VERBOSE:
        print(f"[helpers:wait] Sleeping for {random_number} sec...")
    sleep(random_number)
    if VERBOSE:
        print(f"[helpers:wait] Done.")


def is_full_url(url: str) -> bool:
    if "https://" in url or "http://" in url:
        if VERBOSE:
            print("[helpers:is_full_url] This URL is full, with schema.")
        return True
    if VERBOSE:
        print(
            "[helpers:is_full_url] This URL is not full, just domain name."
        )
    return False


url = argv[1]
file_path = argv[2]

if not is_full_url(url):
    url = f"https://{url}{'' if url.endswith('/') else '/'}"
else:
    if not url.endswith("/"):
        url += "/"

with open(file_path) as openfile:
    words = [
        word.strip()
        for word in openfile.readlines()
        if word.strip()
    ]
    if VERBOSE:
        print(f"[__main__] Readed {len(words)} words from file:\n{words}")

result = {
    "ok": list(),
    "not_ok": list(),
    "time_token_requests": 0,
    "time_token_with_requests_and_waits": 0,
}

for idx, word in enumerate(words, 1):

    if len(word) > MAX_WORD_LENGTH:
        MAX_WORD_LENGTH = len(word)

    start_time = time()
    try:
        if VERBOSE:
            print(
                f"[__main__] Making request to the URL address: {url + word}"
            )
        response = get(url + word)
    except Exception as e:
        raise Exception(f"Bad URL.\nMore data of exception: {e}")
    request_end_time = time()
    if response.status_code == 200:
        if VERBOSE:
            print(f"[__main__] {word} --- OK.")
        result["ok"].append(word)
    else:
        if VERBOSE:
            print(f"[__main__] {word} --- NOT OK!")
        result["not_ok"].append(word)

    # Check for last item, if it's then don't call wait() 
    # function for save time
    if not idx == len(words) - 1:
        wait()

    # Timing
    end_time_with_request_and_wait = time()
    result["time_token_requests"] += request_end_time - start_time
    result["time_token_with_requests_and_waits"] += end_time_with_request_and_wait - start_time

with open(file_path + "_result", "w") as openfile:
    if VERBOSE:
        print("[__main__] Writing file with results...")
    openfile.write(
        f"\nRESULTS OF DATA FROM FILE: {file_path}\n\n"
        f"Requests time token: {result['time_token_requests']} sec.\n"
        f"Total time (with waits): {result['time_token_with_requests_and_waits']} sec.\n"
        f"Free addresses number: {len(result['not_ok'])}\n"
        f"Taken addresses number: {len(result['ok'])}\n"
        f"Total address number: {len(words)}\n\n"
    )

    if VERBOSE:
        print("[__main__] Writing addresses that have 200 status...")
    openfile.write("OK:\n\n")
    for word in result["ok"]:
        openfile.write(
            f"{word} {' ' * (MAX_WORD_LENGTH - len(word))} [{url + word}]\n"
        )

    if VERBOSE:
        print("[__main__] Writing addresses that haven't 200 status...")
    openfile.write("\nNOT OK:\n\n")
    for word in result["not_ok"]:
        openfile.write(
            f"{word} {' ' * (MAX_WORD_LENGTH - len(word))} [{url + word}]\n"
        )

if VERBOSE:
    print("[__main__] Done!")
