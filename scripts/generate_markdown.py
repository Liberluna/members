def remove_start_by_line(string, n: int) -> str:
    return '\n'.join(map(lambda line: line[n:], string.split('\n')))
def get_one_member_markdown_by_member_data(member_data) -> str:
    print(member_data, member_data['post']['isMember'])
    new_line = '\n'
    result = ""
    result += "### {0}\n".format(member_data['names']['ja'])
    
    result += '#### 名前情報\n'
    result += '- `ja`: ' + member_data['names']['ja'] + '\n'
    result += '- `en`: ' + member_data['names']['en'] + '\n'

    result += '#### ロール情報\n'
    result += f'- ' + ('' if member_data['post']['isMember'] else 'サブ') + 'メンバー\n'
    if member_data['post']['isLeader']:
        result += '- リーダー\n'
    if member_data['post']['isModerator']:
        result += '- モデレーター\n'
    
    result += '#### アバター情報\n'
    result += '\n\n<img src="' + member_data['avatar'] + '" width="64" height="64" />\n\n'

    result += remove_start_by_line(f"""
    #### 自己紹介
    ja:
    ```
    { member_data['profile']['ja'] }
    ```
    en:
    ```
    { member_data['profile']['en'] }
    ```
    """[1:-1], 4)
    result += '\n'

    result += '#### Social\n'
    if 'matrix' in member_data['social']:
        result += '- Matrix: [{0}](https://matrix.to/#/{0})\n'.format(member_data['social']['matrix'])
    if 'github' in member_data['social']:
        result += '- GitHub: [{0}](https://github.com/{0})\n'.format(member_data['social']['github'])
    if 'x' in member_data['social']:
        result += '- X(Twitter): [@{0}](https://x.com/{0})\n'.format(member_data['social']['x'])
    if 'scratch' in member_data['social']:
        result += '- Scratch: [{0}](https://scratch.mit.edu/users/{0})\n'.format(member_data['social']['scratch'])
    return result + '\n'
def generate_markdown(data) -> str:
    result: str = ''
    result += '# Liberluna Members Markdown ver.\n'
    result += '⚠️注意 このファイルは自動的に生成されるので、編集しないでください。情報を訂正したい場合は、[members](../members)を編集してください。'
    for member_data in data:
        result += get_one_member_markdown_by_member_data(member_data)
    return result
