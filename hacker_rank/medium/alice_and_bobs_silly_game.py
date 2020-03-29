# For each game, print the name of the winner on a new line. If Alice wins, print Alice; otherwise, print Bob.
import threading

def sillyGame(n):
    def is_divisible(small_number, big_number):
        if big_number % small_number == 0:
            return True
        else:
            return False
    def is_prime(number):
        if number == 2 or number == 3:
            return True
        elif number == 1:
            return False
        else:
            factor = 2
            while factor <= number ** 0.5:
                if is_divisible(factor, number):
                    return False
                    break
                else:
                    factor += 1
            return True
    def SieveOfEratosthenes(n): 
        prime = [True for i in range(n+1)] 
        p = 2
        while(p * p <= n): 
            if (prime[p] == True): 
                for i in range(p * 2, n + 1, p): 
                    prime[i] = False
            p += 1
        c = 0
        for p in range(2, n): 
            if prime[p]: 
                c += 1
        return c 
    def bob_is_winner(number):
        if is_divisible(2, number):
            return True
    length = SieveOfEratosthenes(n + 1)
    if bob_is_winner(length):
        print("Bob")
    else:
        print("Alice")
    return

# arr = list(map(lambda x: 1000000, list(range(1, 1000))))
# for i in arr:
    # print(sillyGame(i))
threads = []
for i in range(1001):
    t = threading.Thread(target=sillyGame, args=(1000,))
    threads.append(t)
    t.start()

    
