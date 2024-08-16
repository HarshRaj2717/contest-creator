import os

import requests


def main():
    rating = int(input("Enter the problem rating to extract: "))
    url = f"https://acodedaily.com/api/v2//ladder?startRating={rating}&endRating={rating + 100}"
    response = requests.get(url)

    try:
        assert response.status_code == 200
        data = response.json()["data"]
        problems = []
        for cur in data:
            problems.append(
                f'https://codeforces.com/contest/{cur["contestId"]}/problem/{cur["index"]}'
            )
        script_path = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_path, f"{rating}.txt")
        with open(output_path, "w") as file:
            for problem in problems:
                file.write(f"{problem}\n")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
