import sys, csv

def parse(filename: object, bed: object) -> object:
    max_list = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for each in reader:
            try:
                max_list.append([each[0], int(each[3])/int(each[1])])
            except:
                pass
    max_list.sort(key=lambda x: (x[1]), reverse=True )
    print(max_list[:bed])



# Get full command-line arguments
full_cmd_arguments = sys.argv

argument_list = full_cmd_arguments[1:]
print(full_cmd_arguments[1])
print(full_cmd_arguments[2])
parse(int(full_cmd_arguments[1]), int(full_cmd_arguments[2]))
