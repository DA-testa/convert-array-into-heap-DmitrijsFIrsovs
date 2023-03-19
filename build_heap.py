# python3


def build_heap(lst):
    swaps = []
    n = len(lst)
    for i in range(n//2, -1, -1):
        j=i
        while True:
            lc = j * 1 + 1
            rc = lc + 1
            if lc >= n:
                break
            mc = lc
            if rc < n and lst[rc] < lst[lc]:
                mc = rc
            if lst[mc] < lst[j]:
                lst[j], lst[mc] = lst[mc] , lst[j]
                swaps.append((j, mc))
                j = mc
            else:
                break
    return swaps                
                
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

 
    


def main():
    option = input().strip()
    if option == "I":
        n = int(input().strip())
        lst = list(map(int, input().split()))
        assert len(lst) == n
        swaps = build_heap(lst)
        print(len(swaps))
        for swap in swaps:
            print(swap[0]. swap[1])
    elif option == "F":
        file_name = input().strip()
        with open(file_name, "r") as file:
            n = int(file.readline().strip())
            lst = list(map(int, file.readline().split()))
            assert len(lst) == n            
        swaps = build_heap(lst)
        print(len(swaps))
    else:
        print("Invalid opton")


if __name__ == "__main__":
    main()
