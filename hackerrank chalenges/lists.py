n = int(input())
arr = list(map(int, input().split()))
# Remove duplicates by converting to a set
unique_scores = list(set(arr))
    
unique_scores.sort(reverse=True)
print(unique_scores[1])