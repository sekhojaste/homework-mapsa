

def prime_checker(num_range):
    prime_nums_list = [2] 
    result = 2
    for num in range(3, num_range):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result += num
            prime_nums_list.append(num)
                

    return result, prime_nums_list


prime_sum, prime_list = prime_checker(14)

print(prime_sum)
print(prime_list)
#albate prime_list ro baraye khoroji niyaz nadashtim, ehtiatan ezafe karadm