# names = ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"]

# birthdates = ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]


def is_birthday_dates(names, birthdates):
    result = []
    for ch in range(0, len(birthdates)):
        month = int(birthdates[ch].split("/")[1])
        if month in [1, 2, 3, 4, 5, 6]:
            # print(names[i])
            result.append(names[ch])
    print(result)


is_birthday_dates(
    ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"],
    ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"],
)
