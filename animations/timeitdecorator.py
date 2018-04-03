    import timeit
    nums = [13, 1, 2, 13, 2, 1, 13]
    def wrapper(func, *args, **kwargs):
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    
    @wrapper(nums)
    def sum13(nums):
      if len(nums) == 0:
        return 0
      for i in range(len(nums)):
        if nums[i] == 13:
          nums[i] = 0
          if i+1 < len(nums):
            nums[i+1] = 0
            i += 2
      return sum(nums)
    
    @wrapper(nums)
    def sum14(nums):
      if len(nums) == 0:
        return 0
      for i in range(len(nums)):
        if nums[i] == 13:
          nums[i] = 0
          if i+1 < len(nums):
            nums[i+1] = 0
      return sum(nums)
    
    # wrapOne = wrapper(sum13, nums)
    # wrapTwo = wrapper(sum14, nums)
    #
    # print(timeit.timeit(wrapOne, number=100000))
    # print(timeit.timeit(wrapTwo, number=100000))
    
    print(timeit.timeit(sum13, number=100000))
    print(timeit.timeit(sum14, number=100000))

    ## list comprehensions/generator expressions ##

    def my_gen():
    for x in range(5)
      yield x

    gen_exp = (x**2 for x in range(5))