
def snake_case_conv(str):
    str_input1_list = str.split("_")
    str_input2_list = []

    for i in str_input1_list:
        str_input2_list.append(i.capitalize())

    return "".join(str_input2_list)

def camel_case_conv(str):
    pass

def case_conv(str):
    pass
