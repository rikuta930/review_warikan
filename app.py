total_amount = int(input('合計金額を入れてね>'))
total_number_of_people = int(input('合計人数を入れてね>'))

amount_per_person = total_amount // total_number_of_people
fraction = total_amount % total_number_of_people

print(f'一人あたりの金額は{amount_per_person}円です｡\n端数は{fraction}円です｡')
