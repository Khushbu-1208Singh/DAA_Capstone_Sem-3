
def knapsack(parcels, capacity):

    n = len(parcels)

    # Create DP table initialized with zeros
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["priority"]

        for w in range(capacity + 1):

            # If parcel cannot fit
            if weight > w:
                dp[i][w] = dp[i - 1][w]

            else:
                # Exclude the parcel
                exclude = dp[i - 1][w]

                # Include the parcel
                include = value + dp[i - 1][w - weight]

                # Choose maximum value
                dp[i][w] = max(include, exclude)

    # Find selected parcels using backtracking
    selected_parcels = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected_parcels.append(parcels[i - 1])

            w -= parcels[i - 1]["weight"]

    selected_parcels.reverse()

    return selected_parcels, dp
