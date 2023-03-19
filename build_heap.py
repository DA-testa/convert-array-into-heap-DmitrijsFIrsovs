# python3


def build_heap(data):
    a = len(data)
    swaps = []
    for i in range(a//2 - 1, -1, -1):
        j = i
        while True:
            lc = j * 2 + 1
            if lc >= a:
                break
            if lc + 1 < a and data[lc+1] < data[lc]:
                lc += 1
            if data[j] > data[lc]:              
                swaps.append((j, lc))
                data[j], data[lc] = data[lc] , data[j]
                j = lc
            else:
                break
                
                
    return swaps                
  

def main():
    option = input()
    if option == 'I':
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    elif option == 'F':
        file = input().strip()
        with open(f'tests/{file}', 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
    else:
        print("Invalid option")
  


if __name__ == "__main__":
    main()
