import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--port", default="5000")

# 1. --port 인자를 받으세요. type=int 를 쓰지 않고, 기본값은 글자 "5000" 입니다

args = parser.parse_args()
print(args.port + "1")

# 2. args.port 에 글자 "1" 을 더한 것을 출력하세요
