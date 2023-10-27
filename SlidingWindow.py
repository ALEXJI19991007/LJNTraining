def all_anagrams(long_str: str, short_str: str):
    result = []
    if len(long_str) == 0 or len(long_str) < len(short_str):
        return result
    # char_count_map的物理意义：
    # char_count_map[x] = n --> we still need to match n 'x'
    char_count_map = get_count(short_str)
    matched_count = 0
    left_ptr = 0
    right_ptr = 0
    while right_ptr < len(long_str):
        cur_char = long_str[right_ptr]
        if cur_char in char_count_map:
            cur_char_count = char_count_map[cur_char]
            # 如果我还需要match一个这样的字母，然后我这里正好extend右边界碰到了这个字母
            if cur_char_count == 1:
                # 那这个字母就被完全match上了
                matched_count += 1
            # 如果这个字母在map里面，无论如何我们都要-1
            char_count_map[cur_char] -= 1
        right_ptr += 1

        # 如果我们的sliding window size已经大于了short_str的size，那我们就需要把左边界向右移动一格
        if right_ptr >= len(short_str):
            # 左边界移动一格，就会有一个最左边character离开我们的sliding window
            char_to_remove = long_str[left_ptr]
            if char_to_remove in char_count_map:
                # 如果最左边的这个character在我们的map里面，我们需要查看这个character目前还需要map几个
                cur_char_count = char_count_map[char_to_remove]
                # 如果目前这个character已经被完全map上了，那如果我们拿走最左边这个character，会导致这个character还需要被match一次
                if cur_char_count == 0:
                    # 所以我们完全match上的count就要-1
                    matched_count -= 1
                # 如果这个字母在map里面，无论如何我们都要+1（i.e.我们需要多match一个）
                char_count_map[cur_char] += 1
            left_ptr += 1
        if matched_count == len(char_count_map):
            result.append(left_ptr)
    return result


def get_count(short_str: str):
    char_count_map = {}
    for c in short_str:
        if c not in char_count_map:
            char_count_map[c] = 0
        char_count_map[c] += 1
    return char_count_map
