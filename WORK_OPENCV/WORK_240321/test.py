## 과제 할 때 시험삼아 테스트해 본 코드들

DEBUG = [0, 1]

if DEBUG[0]:
    def split_string_by_punctuation(text):
        # 온점, 느낌표, 물음표를 기준으로 문자열 분리
        split_text = text.split('.')  # 온점을 기준으로 분리
        split_text = [phrase.split('!') for phrase in split_text]  # 느낌표를 기준으로 분리
        split_text = [subphrase.split('?') for sublist in split_text for subphrase in sublist]  # 물음표를 기준으로 분리

        # 공백 제거
        split_text = [phrase.strip() for sublist in split_text for phrase in sublist if phrase.strip()]

        return split_text


    # 예시 문자열
    text = "Hello, World! How are you? I'm fine. Thanks!"

    # 문자열을 온점, 느낌표, 물음표를 기준으로 나누기
    splitted_text = split_string_by_punctuation(text)
    print(splitted_text)


if DEBUG[1]:
    if '  d  '.strip():
        print('첫번째 발동')

    if 'd'.strip():
        print("두번째 발동")

    if ''.strip():  # 발동 안 함 (''가 반환되기 때문)
        print('세번째 발동')
