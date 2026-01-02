default_time = 60


def training_session(rounds: int) -> None:
    """Workout timer with adjustable countdown"""
    time_per_round = default_time

    def adjust_time() -> None:
        """Adjust time per round"""
        nonlocal time_per_round
        time_per_round -= 5

    for round_num in range(1, rounds + 1):

        if round_num == 1:
            print("Результат:\n"
                  f"Раунд {round_num}: {time_per_round} хвилин ")
        else:
            print(f"Раунд {round_num}: {time_per_round} хвилин після коригування часу")

        if round_num < rounds:
            adjust_time()


training_session(3)
