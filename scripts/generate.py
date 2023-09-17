import yaml, glob, os, json, shutil

members = []
for member_yaml_path in glob.glob('./members/*.yaml'):
    with open(member_yaml_path) as file:
        member_data = yaml.safe_load(file)
        members.append(member_data)

shutil.rmtree('dist')
os.mkdir('dist')

with open('dist/members.json', 'w') as file:
    json.dump(file, members, indent=2)
