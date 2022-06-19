
def main():
    codes = {}
    decoded = ''
    sorted_tuples = sorted(codes.items(), key=lambda item: item[1])
    codes = {k: v for k, v in sorted_tuples}

    k, l = input().split()
    for i in range(int(k)):
        k, f = input().split(': ')
        codes.update({k: f})
    encoded = input()

    for i in range(int(l)):
        for k, v in codes.items():
            if encoded.startswith(v):
                decoded += k
                encoded = encoded[len(v):]
    print(decoded)

if __name__ == '__main__':
    main()
