def foo(x):
    if x <= 1:
        return x
    else:
        n = foo(x-1) + foo(x-2)
        return n


def longest_run(mylist, key):
    counter = 0
    max_count = 1
    for i in range(len(mylist)):
        if key == mylist[i] & mylist[i-1] == mylist[i]:
            counter += 1
            continue
        if counter >= max_count:
            max_count = counter
            counter = 1
        else:
            continue
    return max_count


class Result:
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size  # run on left side of input
        self.right_size = right_size  # run on right side of input
        self.longest_size = longest_size  # longest run in input
        self.is_entire_range = is_entire_range  # True if the entire input matches the key

    def __repr__(self):
        return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
                (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    else:
        mid = len(mylist) // 2
        temp = combine_result(longest_run_recursive(mylist[:mid], key), longest_run_recursive(mylist[mid:], key))
        return temp


def combine_result(left, right):
    if left.is_entire_range:
        if right.is_entire_range:
            temp = Result(left.left_size + right.left_size, left.right_size + right.right_size,
                          left.longest_size + right.longest_size, True)
            return temp
        else:
            temp = Result(left.left_size + right.left_size, right.right_size,
                          max(left.longest_size, right.longest_size),
                          False)
            return temp
    else:
        if right.is_entire_range:
            temp = Result(left.left_size, left.right_size + right.right_size,
                          max(left.longest_size, right.longest_size),
                          False)
            return temp
        else:
            temp = Result(left.left_size, right.right_size,
                          max(left.right_size + right.left_size, left.longest_size,
                              right.longest_size), False)
            return temp


def test_longest_run():
    assert longest_run([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3
    assert longest_run([2, 2, 5, 7, 9, 1, 34, 14, 456, 2], 2) == 2
