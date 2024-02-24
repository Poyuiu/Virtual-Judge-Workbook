file = open("./Beginner_DE.md", "w", encoding="utf-8")

# miscllaneous
file.write(
    "According to a [tutorial](https://codeforces.com/blog/entry/66909) from Codeforces. To become an orange-rated coder, a good training method is to quickly solve the D and E problems of the AtCoder Beginner Contest. This allows oneself to compete with Japanese programmers who excel at fast coding. Therefore, let's take on this speedrun challenge.\n"
)

# Song Yuqi
file.write(
    "\n\n![Alt Text](https://64.media.tumblr.com/e68b0924d47bd82cdb2b6a6e4ab97f32/158ce015e1717a45-c3/s540x810/64cd26694a62ef00bd88996c72916b28b574a350.gif) ![Alt Text](https://64.media.tumblr.com/c76710cbb9aa9056d1d0d294796eee95/158ce015e1717a45-47/s540x810/8a7ba85da1d78c17ca5acca97376c3760965a90c.gif)\n\n"
)

# from 126 to 341 (inclusive) (Feb 19th, 2024)
begin = 126
lastest = 342
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
