file = open("./Beginner_DE.md", "w", encoding="utf-8")

# miscllaneous
file.write(
    "According to a [tutorial](https://codeforces.com/blog/entry/66909) from Codeforces. To become an orange-rated coder, a good training method is to quickly solve the D and E problems of the AtCoder Beginner Contest. This allows oneself to compete with Japanese programmers who excel at fast coding. Therefore, let's take on this speedrun challenge.\n"
)

# Song Yuqi
file.write(
    "\n\n![Alt Text](https://i.pinimg.com/originals/a2/8a/86/a28a86719db56001f029541ea53e2d27.gif)\n\n"
)

# from 126 to 341 (inclusive) (Feb 19th, 2024)
begin = 126
lastest = 341
accumulated_count = 0

for i in range(lastest, begin - 1, -1):
    if i % 10 == 0 or i == lastest:
        file.write(f"#### Round {i} ⬇️\n")
    file.write(f"[problem:AtCoder-abc{i}_d]\n")
    file.write(f"[problem:AtCoder-abc{i}_e]")
    accumulated_count += 2
    if accumulated_count % 10 == 0:
        file.write(str(accumulated_count))
    file.write("\n")
