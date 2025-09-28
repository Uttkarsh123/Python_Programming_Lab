"""
Each video watched generates revenue based on ad impressions:
    1. First 10 views: $0.50 per view
    2. Next 20 views: $0.30 per view
    3. Remaining views: $0.10 per view
You are given hourly views for the day. Calculate total daily revenue.
"""
hourly_views = [18, 25, 35, 8, 41, 19, 5, 10, 22, 30, 14, 57, 27, 6, 12, 16, 39, 17, 9, 24, 19, 17, 26, 31]

total_revenue = 0

for views in hourly_views:
    revenue = 0
    if views <= 10:
        revenue = views * 0.50
    elif views <= 30:
        revenue = 10 * 0.50 + (views - 10) * 0.30
    else:
        revenue = 10 * 0.50 + 20 * 0.30 + (views - 30) * 0.10
    total_revenue += revenue

print(f"Total daily revenue: ${total_revenue:.2f}")