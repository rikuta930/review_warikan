total_amount = int(input('合計金額を入れてね>'))
total_number_of_people = int(input('合計人数を入れてね>'))

print(f'一人あたりの金額は{total_amount // total_number_of_people}円です｡\n端数は{total_amount % total_number_of_people}円です｡')
