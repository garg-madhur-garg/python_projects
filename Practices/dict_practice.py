if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if student_marks[query_name]:
        marks = student_marks.get(query_name)
        print(marks)
        ans = marks[0] + marks[1] + marks[2]
        print(round(ans, 2))