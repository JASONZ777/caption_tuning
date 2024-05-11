import csv, json

# read csv
instruction = 'Please determine whether the traffic scenario described in the input is dangerous or safe'
sft_dataset = []
with open('nonaccident.csv', newline='') as csvfile:
    # csv reader, divide by $
    csvreader = csv.reader(csvfile, delimiter='$')
    for row in csvreader:
        context = row[1]
        response = 'Safe'
        data = {"instruction": instruction, "input": context, "output": response}
        sft_dataset.append(data)

with open("dataset.jsonl", "a", encoding='utf-8') as f:
    for obj in sft_dataset:
        json_line = json.dumps(obj, ensure_ascii=False) + "\n"
        f.write(json_line)
        