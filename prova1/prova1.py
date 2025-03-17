import numpy as np

# exercicio 1

# Carregando o dataset social_media.csv
dataset = np.genfromtxt('social_media.csv', delimiter=';', dtype=str, encoding='utf-8', skip_header=1)


print("Forma do dataset:", dataset.shape)


brazil_count = np.sum(dataset[:, 4] == 'Brazil')


print(f"A quantidade de 'Brazil' que aparece no dataset é: {brazil_count}")

# ====================================================================================================

# exercicio 2

education_count = dataset[dataset[:, 2] == 'Education']

porcentagem = (education_count.shape[0] / dataset.shape[0]) * 100

print(f"A porcentagem de pessoas que possuem 'Education' como formação é: {porcentagem:.2f}%")

# ====================================================================================================

# exercicio 3

instagram_data = dataset[dataset[:, 1] == 'Instagram']

views = instagram_data[:, 5].astype(float)
likes = instagram_data[:, 6].astype(float)

media_views = np.mean(views)
media_likes = np.mean(likes)

instagram_stats = {
    'media_views': media_views,
    'media_likes': media_likes
}

print(f"Média de Views no Instagram: {instagram_stats['media_views']:.2f}")
print(f"Média de Likes no Instagram: {instagram_stats['media_likes']:.2f}")

# ====================================================================================================

# exercicio 4

unique, counts = np.unique(dataset[:, 1], return_counts=True)
platform_post_counts = dict(zip(unique, counts))

max_platform = max(platform_post_counts, key=platform_post_counts.get)
max_posts = platform_post_counts[max_platform]

print(f"A plataforma com maior quantidade de posts é: {max_platform}")
print(f"Número de posts: {max_posts}")

# ====================================================================================================

# exercicio 5

max_likes_index = np.argmax(dataset[:, 6].astype(float))

region_max_likes = dataset[max_likes_index, 4]

print(f"A região de onde saiu o post com maior número de likes é: {region_max_likes}")