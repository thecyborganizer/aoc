recipes = [3, 7]
elf_one = 0
elf_two = 1
def get_new_recipes(n):
    #print (list(map(lambda x: int(x), list(str(n)))))
    return list(map(lambda x: int(x), list(str(n))))

count = 0
target_number = 3000000
while len(recipes) < target_number + 12:
    if count % 1000 == 0:
        print(count)
    count += 1
    recipes.extend(get_new_recipes(recipes[elf_one] + recipes[elf_two]))
    elf_one = (elf_one + recipes[elf_one] + 1) % len(recipes)
    elf_two = (elf_two + recipes[elf_two] + 1) % len(recipes)
#print(recipes, elf_one, elf_two)
print(recipes[target_number:target_number + 10])
solution_str = "".join(list(map(lambda x: str(x), recipes)))
print(solution_str.index("165061"))