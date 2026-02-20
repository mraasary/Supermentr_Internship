"""Assignment (17/02/2026)
   Assignment Name : Logic Builder
   Description : Print numbers 1–50 with Fizz/Buzz logic and count occurrences using loops and functions."""

def fizz_buzz():
    fizz=buzz=fizzbuzz=0
    
    for num in range(1,51):
        if num%3==0 and num%5==0:
            print("FizzBuzz")
            fizzbuzz+=1
        elif num%3==0:
            print("Fizz")
            fizz+=1
        elif num%5==0:
            print("Buzz")
            buzz+=1
        else:
            print(num)
            
    print("\nSummary:")
    print(f"Total Fizz: {fizz}")
    print(f"Total Buzz: {buzz}")
    print(f"Total FizzBuzz: {fizzbuzz}")

if __name__ == "__main__":
    fizz_buzz()
    

            
