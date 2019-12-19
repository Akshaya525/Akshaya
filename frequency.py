def frequencyDigits(n, d): 
    c = 0; 
    while (n > 0): 
        if (n % 10 == d): 
            c += 1;
        n = int(n / 10); 
        return c;
N = 1122322; 
  
# input digit D 
D = 2; 
print(frequencyDigits(N, D));