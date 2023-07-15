hex_list = [
    ")%(<(#0.2B/):/9Q7/>9:P@3BAF\\BCSBIdH:NIRgNVqOHXP`uSg",
    "YUg[KY^]q^f~e[mfewjo",
    "Hey look, a comment!",
    "4|5BRe7S4U-a!Ri",
    "MTQEO4h7q e'Mm4",
    "\"These comments sure do look useful",
    "-Yu09)3\tKfR&Gx~\tF",
    "(I wonder what else I could do with them?",
    "]UZL\\$NnXix]VDE",
    "bB)~bvQ\\w\\WnJlw",
    "Z]4!g$`yyid,glv",
    "44414e54457b673166355f",
    "cXYWnYPNZrK)R\\w",
    "31dBij#|M,,zz&S\tZ",
    "3472335f6d3464335f6279",
    "f7zdPZCw|v4:FN`f{",
    "p2PqFi1Ens&YL(CS",
    "5f626c30636b357d",
    "\\W4eve,F\"]aiB3RYX",
    "bN`Fk6#*Q(AhHgR",
    "%At the edges of the map lies the void"
]

converted_list = []

for hex_str in hex_list:
    decoded_str = bytes.fromhex(hex_str).decode('utf-8')
    converted_list.append(decoded_str)

print(converted_list)
