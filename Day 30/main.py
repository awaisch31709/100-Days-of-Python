# #FieNotFound
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["sdsfsdf"])
# except FileNotFoundError:
#     # print("There was an error")
#     file = open("a_file.txt", "w")
#     file.write("Write Something in It")
# # except KeyError:
# #     print("The key does not exist")
# except KeyError as error_message:
#     print(f"The key{error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File is closed")


height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)