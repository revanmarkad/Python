s = {1, 2, 5, 6}
s2 = {3, 6, 7}

print(s.union(s2))  # s and s2 combination that is union


s.update(s2)  # 3 and 7 added in s becous in s 6 is available but 3 and and 7 not avail
print(s, s2)


cities1 = {
    "Berlin (The Leader)",
    "Tokyo (Hot-Blooded Protagonist)",
    "Helsinki and Oslo (The Loyal Cousins)",
    "Denver (Muscle with a Heart of Gold)",
}

cities2 = {
    "Berlin (The Leader)",
    "Tokyo (Hot-Blooded Protagonist)",
    "Helsinki and Oslo (The Loyal Cousins)",
    "Denver (Muscle with a Heart of Gold)",
    "Moscow (Old and Sensible)",
    "Rio (The Baby)",
    "Nairobi (The Benevolent Matriarch)",
}
cities3 = cities1.intersection(cities2)  # intersection give us common of both;

print(cities3)

cities4 = cities1.symmetric_difference(
    cities2
)  # symmetric_difference give us Uncommon of both;
print(cities4)
