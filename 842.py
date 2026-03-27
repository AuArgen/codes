#
a, t, b = map(int, input().split())
ans = 0
k = []
while ans < 200:
    if len(k) == 0 and a == 0 and b == 0:
        break
    if len(k) and k[0] <= ans:
        k.pop(0)
        ans += 1
        continue
    if b > 0 and t <= ans and a == 0:
        b -= 1
        k.append(ans + 6)
    if a > 0 :
        a -= 1
        k.append(ans + 6)
    ans += 1
print(ans)

# import sys
#
#
# def solve():
#     # Маалыматтарды окуу
#     input_data = input().split()
#     if not input_data:
#         return
#
#     A = int(input_data[0])
#     T = int(input_data[1])
#     B = int(input_data[2])
#
#     # Ылдыйда к?т?п жаткандардын кезеги (алардын келген убактылары)
#     # A адам 0-м?н?тт?, B адам T-м?н?тт? келет
#     q_bot = [0] * A + [T] * B
#
#     # ?ст?нд? ж?рг?нд?рд?н кезеги (алардын т?ш??г? даяр болгон убактылары)
#     q_top = []
#
#     time = 0
#
#     # Эки кезектин биринде эле адам бар болсо, оюн улана берет
#     while q_bot or q_top:
#         # 1-кадам: Т?ш??г? даяр адамдарды текшер?? (Т?ш??г? артыкчылык берилет)
#         if q_top and q_top[0] <= time:
#             q_top.pop(0)  # Адам тепкичтен т?шт?
#             time += 1  # Т?ш?? ?ч?н 1 м?н?т кетти
#             continue  # Тепкич бош эмес болчу, кийинки м?н?тк? ?т?б?з
#
#         # 2-кадам: ?йд? чыгууга даяр адамдарды текшер??
#         if q_bot and q_bot[0] <= time:
#             q_bot.pop(0)  # Адам тепкичке чыгып баштады
#
#             # Бул адам 1 м?н?т чыгат + 5 м?н?т ?ст?нд? болот = 6 м?н?тт?н кийин т?ш??г? даяр
#             ready_to_down_time = time + 6
#             q_top.append(ready_to_down_time)
#             q_top.sort()  # Т?ш?? убактысы боюнча иреттеп коёбуз
#
#             time += 1  # Чыгуу ?ч?н 1 м?н?т кетти
#             continue
#
#         # 3-кадам: Эгерде тепкич бош болуп, бирок эч ким даяр эмес болсо (мисалы T убактысын к?т?п жатсак)
#         # Убакытты дароо кийинки окуяга чейин т?р?б?з
#         next_event = float('inf')
#         if q_top:
#             next_event = min(next_event, q_top[0])
#         if q_bot:
#             next_event = min(next_event, q_bot[0])
#
#         time = next_event
#
#     # Бардык адамдар т?ш?п б?тк?н убакытты чыгарабыз
#     print(time)
#
#
# if __name__ == '__main__':
#     solve()