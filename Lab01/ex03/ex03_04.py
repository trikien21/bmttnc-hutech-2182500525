import ast


def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element


# Nhập tuple từ người dùng (dùng literal_eval thay cho eval để an toàn)
input_tuple = ast.literal_eval(input("Nhập tuple, ví dụ (1, 2, 3): "))
first, last = truy_cap_phan_tu(input_tuple)

# In kết quả
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)
