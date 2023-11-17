def minimum_beer_types_dp(workers, beer_types, preferences):
    preference_matrix = [[1 if pref == 'Y' else 0 for pref in worker_prefs] for worker_prefs in preferences]

    total_combinations = 1 << workers

    dp = {0: 0}

    for mask in range(total_combinations):
        if mask not in dp:
            continue

        for beer in range(beer_types):
            new_mask = mask
            for worker in range(workers):
                if preference_matrix[worker][beer] == 1:
                    new_mask |= (1 << worker)

            if new_mask in dp:
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
            else:
                dp[new_mask] = dp[mask] + 1

    final_mask = (1 << workers) - 1
    

    return dp.get(final_mask, float('inf'))

if __name__ == "__main__":
    print(minimum_beer_types_dp(6, 3, ["YNN", "YNY", "YNY", "NYY", "NYY", "NYN"]))
