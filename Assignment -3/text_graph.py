"""
You are a data analyst at a streaming platform, managing user interactions, analytics,
and daily operations. Use a for loop to create a text-based graph of hourly views. For
example, use * to represent every 5 views.
"""
hourly_views = [12, 25, 33, 8, 41, 19, 5, 10, 22, 30, 14, 50]

print("Hourly Views Graph (1 * = 5 views):\n")

for hour, views in enumerate(hourly_views):
    stars = '*' * (views // 5)
    print(f"Hour {hour:02}: {stars}")
