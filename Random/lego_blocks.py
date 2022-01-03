'''
******************* PROBLEM STATEMENT
LC # https://www.hackerrank.com/challenges/one-week-preparation-kit-lego-blocks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-six

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
#DP
'''

'''
    This problem is very hard to follow
    Pasted sample solution below
'''
def legoBlocks(n, m):
    # Write your code here
    M = 1000000007

    a = [0,1,2,4,8] # a[i] is the number of ways to create walls with width i. For example: for wdth 3 there are 4 ways to create walls w. that width
    for j in range(5,m+1):  # this formula executes only when we have width 5 or more
        a.append((a[j-1]+a[j-2]+a[j-3]+a[j-4])%M) # Addinf the last 4 possible ways returns the total number of ways! How is that possible
    
    for i in range(m+1): # this will give us all the walls for height n 
        a[i] = pow(a[i],n,M)

    # let r[i] be the number of good layouts that have height n, and width i
    r = [a[i] for i in range(m+1)] # start with all of them 
    for i in range(1,m+1):
        for j in range(1,i):
            r[i] -= (r[j]*a[i-j]) # subtract the number of bad layouts, when the FIRST vertical break in the wall appears at index j 
        r[i] = r[i]%M # make the computations easier 
    return r[m]