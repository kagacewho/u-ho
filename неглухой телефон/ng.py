input_data = open('input.txt', 'r') 
data = input_data.read()
s = int(data)
out = s
output_data = open('output.txt', 'w')
output_data.write(str(out))
input_data.close()
output_data.close()