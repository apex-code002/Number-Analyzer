from colorama import Fore, Style, init
init(autoreset=True)

# ------------------------------------
# Number Property Check Functions
# ------------------------------------
def is_even(n): return n % 2 == 0
def is_odd(n): return n % 2 != 0

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    s = str(abs(n))
    return s == s[::-1]

def is_perfect_square(n):
    if n < 0: return False
    return int(n**0.5) ** 2 == n

def is_armstrong(n):
    s = str(abs(n))
    return abs(n) == sum(int(d)**len(s) for d in s)

def is_perfect(n):
    if n < 2: return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# ------------------------------------
# Number Analysis
# ------------------------------------
def analyze_number(n):
    print(Fore.CYAN + f"\n🔍 ANALYZING NUMBER: {n}")
    print(Fore.WHITE + "-" * 35)
    
    print(f"Even:              {is_even(n)}")
    print(f"Odd:               {is_odd(n)}")
    print(f"Prime:             {is_prime(n)}")
    print(f"Palindrome:        {is_palindrome(n)}")
    print(f"Perfect Square:    {is_perfect_square(n)}")
    print(f"Armstrong:         {is_armstrong(n)}")
    print(f"Perfect Number:    {is_perfect(n)}")

# ------------------------------------
# Save Report to File
# ------------------------------------
def save_report(nums):
    with open("number_report.txt", "w") as f:
        f.write("=========== NUMBER ANALYZER PRO REPORT ===========\n\n")

        for n in nums:
            f.write(f"Number: {n}\n")
            f.write(f"  Even: {is_even(n)}\n")
            f.write(f"  Odd: {is_odd(n)}\n")
            f.write(f"  Prime: {is_prime(n)}\n")
            f.write(f"  Palindrome: {is_palindrome(n)}\n")
            f.write(f"  Perfect Square: {is_perfect_square(n)}\n")
            f.write(f"  Armstrong: {is_armstrong(n)}\n")
            f.write(f"  Perfect Number: {is_perfect(n)}\n\n")

        f.write("=========== END OF REPORT ===========")

    print(Fore.GREEN + "\n💾 Report saved as 'number_report.txt'")

# ------------------------------------
# MENU-DRIVEN MAIN PROGRAM
# ------------------------------------
def main():
    print(Fore.GREEN + "===================================")
    print("        🧮 NUMBER ANALYZER PRO")
    print("===================================" + Style.RESET_ALL)

    numbers = input(Fore.YELLOW + "Enter numbers separated by space: " + Style.RESET_ALL).split()
    nums = []

    # Validate numbers
    for num in numbers:
        try:
            n = int(num)
            nums.append(n)
            analyze_number(n)
        except ValueError:
            print(Fore.RED + f"⚠ '{num}' is NOT a valid integer!")

    if not nums:
        print(Fore.RED + "\n❌ No valid numbers entered!")
        return

    # Summary
    print(Fore.MAGENTA + "\n📊 SUMMARY")
    print(Fore.WHITE + "-" * 30)
    print(f"Total numbers:           {len(nums)}")
    print(f"Even numbers:            {sum(is_even(x) for x in nums)}")
    print(f"Odd numbers:             {sum(is_odd(x) for x in nums)}")
    print(f"Prime numbers:           {sum(is_prime(x) for x in nums)}")
    print(f"Palindrome numbers:      {sum(is_palindrome(x) for x in nums)}")
    print(f"Armstrong numbers:       {sum(is_armstrong(x) for x in nums)}")
    print(f"Perfect numbers:         {sum(is_perfect(x) for x in nums)}")

    # Save Report
    save_report(nums)


if __name__ == "__main__":
    main()
