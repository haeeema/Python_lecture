PI = 3.14159


def number_input():
    return float(input('숫자 입력> '))


def get_circumference(radius):
    return 2 * PI * radius


def get_area(radius):
    return PI * radius * radius


def print_name():
    print(__name__)


# python entry_module.py와 같이 실행될 경우에는
# __name__ 변수에 __main__이 저장되므로 if문이 실행됨
if __name__ == '__main__':
    print('원의 반지름: ', number_input())
    print(
        f'원의 둘레: {get_circumference(number_input()):.4f}, 원의 넓이: {get_area(number_input()):.4f}')
