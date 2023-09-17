import yaml, glob, os, json, shutil

members = []
for member_yaml_path in glob.glob('./members/*.yaml'):
    with open(member_yaml_path) as file:
        member_data = yaml.safe_load(file)
        members.append(member_data)

try:
  shutil.rmtree('dist')
except FileNotFoundError:
    pass

os.mkdir('dist')

with open('dist/members.json', 'w') as file:
    json.dump(members, file, indent=2, ensure_ascii=False)

typescript_code = """
import data from './members.json' assert { type: 'json' }
import type { Member } from '../member'

export default data as Member
""".strip()
with open('dist/members.ts', 'w') as file:
    file.write(typescript_code)

python_code = f"""
# For Raw JSON
true = True
false = False

# Define Data from JSON
members = {json.dumps(members, indent=4, ensure_ascii=False)}
""".strip()
with open('dist/members.py', 'w') as file:
    file.write(python_code)
