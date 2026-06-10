# # Create the file (only once, 'x' mode will error if file exists)
# y = open("panada.txt", "x")
# y.close()

# # Append text to the file
# with open("panada.txt", "a") as y:
#     y.write("hello my dear friend , i am joe ")

# # Read the file content
# with open("panada.txt", "r") as y:
#     print(y.readline())


with open("panada.txt","a") as y:
    y.write("your friend is waiting for you ")
with open("panada.txt","r") as y:
    print(y.read())