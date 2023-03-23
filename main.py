
file_names = ['1.txt', '2.txt', '3.txt']
files_data = []

for file_name in file_names:
    with open(file_name) as f:
        lines = f.readlines()
        num_lines = len(lines)
    files_data.append({'name': file_name, 'num_lines': num_lines, 'content': lines})

files_data.sort(key=lambda x: x['num_lines'])

with open('result.txt', 'w') as f:
    for file_data in files_data:
        f.write('\n' + file_data['name'] + '\n')
        f.write(str(file_data['num_lines']) + '\n')
        for line in file_data['content']:
            f.write(line)

    