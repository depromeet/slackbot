def parse_command(command):
    """
    @<USERID> 을 제외한 실제 명령어를 리턴해준디.
    :param command: 명령어. @<USERID> <텍스트> 형태로 나타난다.
    :return: @<USERID> 을 제외한 나머지 텍스트
    """
    actual_command = command[12:] if command[12] != ' ' else command[13:]
    return actual_command
