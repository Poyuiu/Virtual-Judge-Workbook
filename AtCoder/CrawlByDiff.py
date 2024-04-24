import requests
import json


def crawl_and_parse(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            problems = []
            for problem_name, attributes in data.items():
                difficulty = attributes.get("difficulty")
                is_experimental = attributes.get("is_experimental")
                if difficulty is not None and not is_experimental:
                    problems.append((problem_name, difficulty))
            return problems
        else:
            print("Failed to fetch data from the URL:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None


def main():
    url = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    problems = crawl_and_parse(url)
    if problems:
        problems.sort(key=lambda x: x[1])

        file = open("./CrawlByDiff.md", "w", encoding="utf-8")

        file.write(
            r"API: https://kenkoooo.com/atcoder/resources/problem-models.json" + "\n\n"
        )

        file.write("不知道有什麼方法可以篩掉日文題(可CC解惑)\n\n")

        file.write("#### 目錄\n")
        file.write("* [<1000](#<1000)\n")
        for i in range(1000, 3200, 200):
            file.write(f"* [{i}](#{i})\n")
        file.write("* [3200](#3200)\n")

        idx: int = 0

        def write_problems(difficulty: int):
            nonlocal idx
            while idx < len(problems) and problems[idx][1] < difficulty:
                file.write("[problem:AtCoder-" + problems[idx][0] + "]\n")
                idx += 1

        file.write(f"\n#### < 1000\n")
        write_problems(1000)

        for difficulty in range(1000, 3200, 200):
            file.write(f"\n#### {difficulty}\n")
            write_problems(difficulty + 200)

        file.write("\n#### 3200\n")
        while idx < len(problems):
            file.write("[problem:AtCoder-" + problems[idx][0] + "]\n")
            idx += 1


if __name__ == "__main__":
    main()
