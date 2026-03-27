import sys


def solve():
    # Маалыматты тез окуу
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]

    # Латын алфавитиндеги үндүү тамгалар (Y да кирет, анткени акыркы сөз ZZZZZY)
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

    # DFS (Рекурсивдүү издөө) функциясы
    def dfs(index, current_prefix, is_greater, vowel_used):
        # Сөз 6 тамгага жеткенде текшеребиз
        if index == 6:
            # Эгерде сөз берилген сөздөн чоң болсо жана кеминде 1 үндүү тамга камтыса
            if is_greater and vowel_used is not None:
                return current_prefix
            return None

        # Эгерде сөз чоңоё элек болсо, берилген сөздүн тамгасынан баштайбыз
        # Эгерде чоңоюп кеткен болсо, анда эң кичинекей 'A' тамгасынан баштайбыз
        start_char = 'A' if is_greater else s[index]

        for char_code in range(ord(start_char), ord('Z') + 1):
            char = chr(char_code)
            new_vowel_used = vowel_used

            # Эгерде тамга үндүү болсо
            if char in vowels:
                # Эгерде мурун башка үндүү тамга колдонулган болсо, бул бутакты токтотобуз
                if vowel_used is not None and char != vowel_used:
                    continue
                new_vowel_used = char

            # Учурдагы сөз берилген сөздөн чоң болдубу аныктайбыз
            new_is_greater = is_greater or (char > s[index])

            # Кийинки тамгага өтүү
            res = dfs(index + 1, current_prefix + char, new_is_greater, new_vowel_used)

            # Эгерде туура сөз табылса, аны дароо кайтарабыз
            if res is not None:
                return res

        return None

    # Издөөнү баштоо
    ans = dfs(0, "", False, None)
    if ans:
        print(ans)


if __name__ == '__main__':
    solve()