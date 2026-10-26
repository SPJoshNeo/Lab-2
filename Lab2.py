import statistics as stat

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Number List: "+ str(num_list))
    print('Average: '+ str(calc_average(num_list)))
    print('Min and Max: '+ str(find_min_max(num_list)))
    print('Median: '+ str(calc_median_temperature(num_list)))

def display_main_menu():
    print('display_main_men')

def get_user_input():
#    x=1
#    while x!=0:
#        y=input("Number "+str(x)+" input (type 0 to exit): ")
#        if int(y)==0:
#            x=0
#    print("exit loop")

    input_list=input("Enter numbers, having a comma ',' to seperate each number: ")
    num_list=[float(x) for x in input_list.split(",")]
    return num_list

def calc_average(num_list):
    print('calc_average')
    num_ave = sum(num_list)/len(num_list)
    return float(num_ave)

def sort_temperature(num_list):
    num_list.sort()
    return num_list

def find_min_max(num_list):
    return [min(num_list),max(num_list)]

def calc_median_temperature(num_list):
    num_list=sort_temperature(num_list)
    median_num=stat.median(num_list)
    return median_num

if __name__ == "__main__":
    main()