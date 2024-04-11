# Function to generate prime numbers within a given range
def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

# Main function
def main():
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    guess = int(input("Guess the number of prime numbers: "))
    
    primes = generate_primes(start_range, end_range)
    if primes:
        if len(primes) == guess:
            print("Got it!")
            print(len(primes))
        else:
            print("Got you looking, but the amount was: ", len(primes))
            print("Prime numbers within the range:", primes)
    else:
        print("No prime numbers found within the specified range.")

if __name__ == "__main__":
    main()
