products_list = [("iphone",5800),
        ('mac Pro', 980),
        ('watch', 500),
        ('Coffee',31),
        ('python_book', 120),
        ] 

salary = input("Input your salary : ")
shopping_list = []
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(products_list):
            print(index,item)
        user_choice = input("mai nage >>> : ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if 0 <= user_choice <= len(products_list):
                p_item = products_list[user_choice]
                if p_item[1] <= salary: # mai de qi
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart ,your current balance is \033[31;1m%s\033[0m"%(p_item, salary))
                else:
                    print("\033[41;1m your balance is not enough!\033[0m")
            else:
                print("product code [%s] item is not exist." % user_choice)
        elif user_choice == 'q':
            print("your shopping cart is :")
            for p in shopping_list:
                print(p)
            print("your balance is \033[31;1m%s\033[0m"%salary)
            exit()

        else:
            print("invalid option")


