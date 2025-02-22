import sys


def total_salary(path):
    lines = []

    try:
        with open(path) as file:
                while True:
                    line = file.readline()

                    if not line:
                        break

                    _, salary_str = line.split(',')

                    if not salary_str:
                        print("No salary found")

                    salary = parse_salary(salary_str)

                    lines.append(salary)
    except Exception as e:
        print(e)

    items_count = len(lines)

    if items_count == 0:
        return 0, 0

    total = sum(lines)
    average = int(total / items_count)

    return total, average

def parse_salary(salary_str):
    try:
        return int(salary_str.strip())
    except Exception as e:
        print(e)
        return 0

def main():
    path = sys.argv[1]
    total, average = total_salary(path)
    print(f"Total: {total}, Average: {average}")

if __name__ == "__main__":
    main()