for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break

for num in range(2,10):
    if num % 2 == 0:
        print(f"{num} is an even number")
        continue
    print(f"{num} is an odd number")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(f"{n} is a prime number")

def https_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 405:
            return "Method Not Allowed"
        case _:
            return "Unknown Error"
        
print(https_error(404))