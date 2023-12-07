questions = [
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is",
        "Sep 8",
        "Nov 28",
        "may 28",
        "Jan 2",
        1,
    ],
]


levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

money = 0

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuaction for Rs. {levels[i]}")
    print(f"a. {question[1]}        b. {question[2]} ")
    print(f"c. {question[3]}        d. {question[4]} \n ")
    print("Quit Press 0")
    reply = int(input("Enter your answer 1 to 4  :"))

    if reply == 0:
        print("You are Quit 🙏")
        break
    if reply == question[-1]:
        print(f"Corruct Answer , you have own Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 3200000
        elif i == 14:
            money = 10000000

    else:
        print("!!!!!!!!!!!  Wrong Answer  !!!!!!!!!!!!!!!")
        break


print(f"Your take home money is {money}")
