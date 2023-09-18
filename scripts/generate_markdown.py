def get_one_member_markdown_by_member_data(member_data) -> str:
    result = f"""
    ### {member_data['names']['ja']}
    #### 名前情報
    - ja: {member_data['names']['ja']}
    - en: {member_data['names']['en']}
    #### ロール情報
    - { '' if {member_data['post']['isMember']} else 'サブ' }メンバー
    """.strip()
    return result + '\n'
def generate_markdown(data) -> str:
    result: str = ''
    result += '# Liberluna Members Markdown ver.\n'
    for member_data in data:
        result += get_one_member_markdown_by_member_data(member_data)
    return result
