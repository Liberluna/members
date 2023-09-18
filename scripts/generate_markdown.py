def get_one_member_markdown_by_member_data(member_data) -> str:
    print(member_data, member_data['post']['isMember'])
    result = f"""
    ### {member_data['names']['ja']}
    #### 名前情報
    - `ja`: {member_data['names']['ja']}
    - `en`: {member_data['names']['en']}
    #### ロール情報
    - { '' if {member_data['post']['isMember']} else 'サブ' }メンバー
    { '- リーダー\n' if member_data['post']['isLeader'] }{ '- モデレーター\n' if member_data['post']['isModerator'] }
    #### アバター情報
    
    <img src="{member_data['avatar']}" width="64" height="64" />

    #### 自己紹介
    ja:
    ```
    { member_data['profile']['ja'] }
    ```
    en:
    ```
    { member_data['profile']['en'] }
    ```
    #### ソーシャル
    - 
    """
    result = '\n'.join(map(lambda line: line[3:], result[1:-1].split('\n')))
    return result + '\n'
def generate_markdown(data) -> str:
    result: str = ''
    result += '# Liberluna Members Markdown ver.\n'
    for member_data in data:
        result += get_one_member_markdown_by_member_data(member_data)
    return result
