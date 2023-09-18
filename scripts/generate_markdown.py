def remove_start_by_line(string, n: int) -> str:
    return '\n'.join(map(lambda line: line[n:], string.split('\n')))
def get_one_member_markdown_by_member_data(member_data) -> str:
    print(member_data, member_data['post']['isMember'])
    new_line = '\n'
    result = ""
    result += "### {member_data['names']['ja']}\n"
    
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
    result += '<img src="' + member_data['avatar'] + '"width="64" height="64" />\n'

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
    return result + '\n'
def generate_markdown(data) -> str:
    result: str = ''
    result += '# Liberluna Members Markdown ver.\n'
    for member_data in data:
        result += get_one_member_markdown_by_member_data(member_data)
    return result
