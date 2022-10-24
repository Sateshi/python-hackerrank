def is_leap(year):
    leap = False
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)

def main():
    print(is_leap(1900))
    print(is_leap(2004))
    
if __name__ == "__main__":
    main()