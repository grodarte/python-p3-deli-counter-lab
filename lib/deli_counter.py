katz_deli = []

def line(cust_list):
    if len(cust_list) == 0:
        print("The line is currently empty.")
    else:
        line_update =  "The line is currently:"
        for index, name in enumerate(cust_list):
            line_update += f" {index + 1}. {name}"
        print(line_update)
    
def take_a_number(cust_list, new_cust):
    cust_list.append(new_cust)
    print(f"Welcome, {new_cust}. You are number {len(cust_list)} in line.")

def now_serving(cust_list):
    if len(cust_list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {cust_list[0]}.")
        cust_list.pop(0)
    