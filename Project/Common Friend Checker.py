 def is_common_friend(user, friends_a, friends_b):
    is_friend_a = friends_a.count(user) >= 1
    is_friend_b = friends_b.count(user) >= 1
    is_common = is_friend_a & is_friend_b

    return is_common


friend_gilang = ["Adul", "Sam"]
friend_riza = ["kai", "axel"]
common_axel = is_common_friend("axel", friend_gilang, friend_riza)

print(f"Axel is a common friend : {common_axel}")