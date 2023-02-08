name = "Игорь"
height = 1.75
weight = 54
bmi = weight / (height ** 2)
print("индекс массы тела: " + str(bmi))

if bmi < 25:
    print("У " + name + " нет лишнего веса")
else:
    print("У " + name + " есть лишний вес") 