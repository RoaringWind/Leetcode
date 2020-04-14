import sys
sys.setrecursionlimit(100000)
class Solution:
    def numOfWays(self, n: int) -> int:
        matrix=[None]*3
        ans=0
        def sear(m,a):
            nonlocal n,ans
            if a==n*3:
                ans+=1
                return
            x=a//3
            y=a%3
            a+=1
            t=m.copy()
            temp=[1,2,3]
            if x==0 and y==0:
                for i in temp:
                    t[y]=i
                    sear(t,a)
            elif x==0:
                temp.remove(t[y-1])
                for i in temp:
                    t[y]=i
                    sear(t,a)
            elif y==0:
                temp.remove(t[y])
                for i in temp:
                    t[y]=i
                    sear(t,a)
            else:
                if t[y] in temp:
                    temp.remove(t[y])
                if t[y-1] in temp:
                    temp.remove(t[y-1])
                for i in temp:
                    t[y]=i
                    sear(t,a)
        sear(matrix,0)
        return ans%(10**9+7)
A=Solution()
aaa=[]
# for i in range(1,5001):
#     aaa.append(A.numOfWays(i))
#     print("now:",i)
print(A.numOfWays(10))
