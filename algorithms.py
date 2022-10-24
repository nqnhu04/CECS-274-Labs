"""Implementations of some sorting"""
import random


def merge(a0, a1, a):
    i0 = i1 = 0
    for i in range(len(a)):
        if i0==len(a0):
            a[i] = a1[i1]
            i1+=1
        elif i1==len(a1):
            a[i]=a0[i0]
            i0+=1
        elif a0[i0]<=a1[i1]:
            a[i] = a0[i0]
            i0+=1
        else:
            a[i]=a1[i1]
            i1+=1

def merge_sort(a):
    if len(a)<=1:
        return a
    m = len(a)//2
    a0 = merge_sort(a[0:m])
    a1 = merge_sort(a[m:len(a)])
    merge(a0,a1,a)
    return a

def _quick_sort(a, i, n):
    if n<=1:
        return
    x = a[i+random.randint(0,n-1)]
    p,j,q = i-1,i,i+n
    while j<q:
        if a[j]<x:
            p+=1
            a[j],a[p] = a[p],a[j]
            j+=1
        elif a[j]>x:
            q-=1
            a[j],a[q] = a[q],a[j]
        else:
            j+=1
        _quick_sort(a, i, p-i+1)
        _quick_sort(a, q, n-(q-i))


def quick_sort(a):
    _quick_sort(a, 0, len(a))
    

def binary_search(a, n, x) :
    if len(a)==0:
        return -1
    l = 0
    r = n-1
    while r>l:
        m = (l+r)//2
        if x<=a[m]: 
            r=m
        else:
            l=m+1
    return l #return index
