print('Введите пункт меню:')
t = {
    "Создать": "Этот пункт в разработке",
    "Найти": "Этот пункт в разработке",
    "Отредактировать": "Этот пункт в разработке",
    "Удалить": "Этот пункт в разработке",
    "Выйти": "Этот пункт в разработке"
}
for x in t:
  print(x)

a = str(input())
if a == "Выйти":
    import mymodule

    mymodule.Exit_program()
elif a != "Выйти":
    print(t[a])