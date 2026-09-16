def min_weights(weights):
    weights.sort(reverse=True)   # largest first
    total = sum(weights)
    
    left_sum = 0
    count = 0
    
    for w in weights:
        left_sum += w
        count += 1
        
        if left_sum > total - left_sum:
            return count
            
print(min_weights([1,1,1,1,1,1,1,1,1,10]))