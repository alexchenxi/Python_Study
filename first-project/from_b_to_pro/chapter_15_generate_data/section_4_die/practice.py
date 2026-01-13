from die import Die
import plotly.express as px


def two_dice_eight():
    die_1 = Die(8)
    die_2 = Die(8)
    results = []
    for _ in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    poss_results = range(1, max_result + 1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    title = "Results of rolling two D8 1000 times"
    label = {"x": "Result", "y": "Frequency of Result"}
    fig = px.bar(
        x=poss_results,
        y=frequencies,
        title=title,
        labels=label,
    )
    fig.update_xaxes(dtick=1)
    fig.show()


def three_dice_six():
    die_1 = Die(6)
    die_2 = Die(6)
    die_3 = Die(6)
    results = [die_1.roll() + die_2.roll() + die_3.roll() for _ in range(1000)]

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    poss_results = range(1, max_result + 1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    title = "Results of rolling three D6 1000 times"
    label = {"x": "Result", "y": "Frequency of Result"}
    fig = px.bar(
        x=poss_results,
        y=frequencies,
        title=title,
        labels=label,
    )
    fig.update_xaxes(dtick=1)
    fig.show()


# two_dice_eight()
three_dice_six()
