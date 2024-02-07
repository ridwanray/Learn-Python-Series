# file_object = open(file_name, access_mode)
# file_object = open("sample.txt","r")
# file_data = file_object.readlines()
# print(type(file_data))
# print(file_data)
# for line in file_data:
#     print(line.strip())
# file_object.close()
# with open("sample.txt","r") as file_object:
#     file_data = file_object.readlines()
#     for line in file_data:
#         print(line.strip())

#write mode
# with open("sample2.txt", "w") as file_object:
#     # file_object.write("Hi")
#     # file_object.write("Hi")
#     # file_object.write("Hi")
#     file_object.writelines(["hi\n", "hi\n"])

# print("done")

# append mode
# with open("sample2.txt", "a") as file_object:
#     file_object.write("\nHi")

# print("Done!")
# csv format
# import csv

# with open("sample.csv", "r") as file_object:
#     reader = csv.reader(file_object)
#     next(reader)
#     for name, level in reader:
#         print(F"{name}:{level}")

#csv -writing
import csv

with open("sample2.csv", "w") as file_object:
    writer = csv.writer(file_object)
    writer.writerow(["Name", "Level"])
    writer.writerow(["Ray", "10"])
    writer.writerow(["Bob", "10"])
        










