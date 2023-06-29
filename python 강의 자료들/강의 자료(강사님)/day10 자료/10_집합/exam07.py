# 집합을 사용하여 여러 사람들이 좋아하는 영화 목록에서 
# 공통으로 좋아하는 영화를 찾고, 
# 개인별로만 좋아하는 영화를 찾는 프로그램

# 각 사람이 좋아하는 영화 목록
alice_movies = {"The Shawshank Redemption", "Pulp Fiction", "The Godfather", "Inception"}
bob_movies = {"The Godfather", "Forrest Gump", "Inception", "The Matrix"}
charlie_movies = {"The Shawshank Redemption", "The Godfather", "The Matrix", "Forrest Gump"}

# 공통으로 좋아하는 영화 찾기
common_movies = alice_movies & bob_movies & charlie_movies
print("Common movies:", common_movies)

# 개인별로만 좋아하는 영화 찾기
alice_unique_movies = alice_movies - bob_movies - charlie_movies
print("Alice's unique movies:", alice_unique_movies)

bob_unique_movies = bob_movies - alice_movies - charlie_movies
print("Bob's unique movies:", bob_unique_movies)

charlie_unique_movies = charlie_movies - alice_movies - bob_movies
print("Charlie's unique movies:", charlie_unique_movies)
