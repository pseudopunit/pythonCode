with open('demo.txt', 'w') as fh:
    for i in range(10):
        fh.write('This is line no %d\n' % (i + 1))

# with automatically closes the file-handler
with open('demo.txt', 'r') as fh:
    for line in fh:
        print(line)

# saving json file
import json
a = {
    'name': 'Punit',
    'age': 21,
    'marks': [50, 48, 43, 47],
    'object': {
        'colour': ('grey', 'black')
    }
}
with open('demo.json', 'w') as fh:
    fh.write(json.dumps(a, indent=4))

with open('demo.json', 'r') as fh:
    json_str = fh.read()
    json_value = json.loads(json_str)
    print(json_value['name'])
    print(json_value['object'])