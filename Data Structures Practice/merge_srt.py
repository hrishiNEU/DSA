class Solution:
    def sort(arr):
        length = len(arr)
        mid = length//2

        left = arr[mid:]
        right = arr[:mid]

        