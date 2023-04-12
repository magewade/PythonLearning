input_string = input().split(" ")
num_chunks = int(input())
list_of_chunks = []
for i in range(0, len(input_string), num_chunks):
    list_of_chunks.append(input_string[i:i+num_chunks])

print(list_of_chunks)