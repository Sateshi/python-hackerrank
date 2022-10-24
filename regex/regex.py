import re

def main():
    n = int(input())
    for _ in range(n):
        if(re.search("^[789]\d{9}$",input())):
            print("YES")
        else:
            print("NO")
            
if __name__ == "__main__":
    main()