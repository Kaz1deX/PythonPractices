import math
import matplotlib.pyplot as matplotlib


# Задание 1
def main1(n, m):
    result = 0
    temp_result = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            temp_result += 42*j+90*(j**4)-8
    temp_result /= 31
    for i in range(1, n+1):
        for j in range(1, m+1):
            result += (math.ceil(i) - 76*j)
    return 22*result-temp_result


# print(f"{main1(88, 80):.2e}")
# print(f"{main1(21, 83):.2e}")


# Задание 2
def main(n):
    if n == 0:
        return 6
    if n == 1:
        return 4
    return 1/45*(main(n-2)**3)+(math.cos(main(n-1)))


# print(f"{main(12):.2e}")
# print(f"{main(2):.2e}")


# Задание 3
def main3(y, z):
    n = len(y)
    result = 0
    for i in range(n):
        result += (y[i] - z[i])**2
    result = math.sqrt(result)
    return result


# print(f"{main3([1,  0.5, 1], [0.5, 2, 1]):.2e}")


# Задание 4
def main4(y, z):
    n = len(y)
    result = 0
    for i in range(n):
        result += abs(y[i] - z[i])
    return result


# print(f"{main4([1,  0.5, 1], [0.5, 2, 1]):.2e}")


# Задание 5
def main5(y, z):
    n = len(y)
    maxim = 0
    for i in range(n):
        temp_maxim = abs(y[i] - z[i])
        if temp_maxim > maxim:
            maxim = temp_maxim
    return maxim


# print(f"{main5([1,  0.5, 1], [0.5, 2, 1]):.2e}")


# Задание 6
def main6(y, z):
    result = 0
    n = len(y)
    for i in range(n):
        result += (y[i]-z[i])**2
    result = math.sqrt(result)
    return result


# print(f"{main6([1,  0.5, 1], [0.5, 2, 1]):.2e}")


# Задание 7
def main7(y, z):
    h = 5
    result = 0
    for i in range(0, len(y)):
        result += abs((y[i]-z[i])**h)
    return result**(1/h)


# print(f"{main7([1, 0.5, 1], [0.5, 2, 1]):.3e}")


# Задание 8
def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = matplotlib.subplots()
    # построение гистограммы с подписями
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])


# distance_metrics = [main3, main4, main5, main6, main7]
# visualize(distance_metrics, [1, 0.5, 1], [0.5, 2, 1], 2)
# matplotlib.show()


# Задание 9(1)
def reverse1(words):
    n = len(words)
    result = ""
    for i in range(n):
        if i != 0:
            result += " "
        result += words[n - i - 1]
    return result


# print(reverse1(["language!", "programming", "Python", "the", "love", "I"]))


# Задание 10
def main10(s, c):
    count_c = 0
    for i in s:
        if i == c:
            count_c += 1
    return count_c


def count_characters(s):
    d = {}
    s = s.lower()
    for i in range(len(s)):
        if i != ' ':
            d[s[i]] = main10(s, s[i])
    return d


s = reverse1(["language!", "programming", "Python", "the", "love", "I"])
# print(count_characters(s))


# Задание 11
def main11(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return main11(a, b, i - 1, j - 1)
    else:
        return 1 + min(main11(a, b, i - 1, j), main11(a, b, i, j - 1), main11(a, b, i - 1, j - 1))


# print(main11('Hello, world!', 'Goodbye, world!', 1, 2))
