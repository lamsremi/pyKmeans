"""K-means Clutering implementation in pure python using Lloyd's algorithm.
"""
import random


class Observation(list):
    """An observation."""
    def __init__(self, row=[], mean=None):
        list.__init__(self, row)
        self.mean = mean


class Mean(list):
    """An observation."""
    def __init__(self, row=[], id_mean=None):
        list.__init__(self, row)
        self.id = id_mean


def fit(rows, k_value=20, threshold=0.1):
    """Compute the means.
    Args:
        rows (list): dataset to cluster.
        k_value (int): number of means.
        threshold (float): condition to stop the iteration process.
    Return:
        means (list): the k means.
    """
    # Observations
    observations = [Observation(row) for row in rows]

    # Initialise the means
    means = init_means("forgy", observations, k_value, Mean)

    # Initialize the moving distances
    moving_distances = [random.randint(0,100) for x in range(k_value)]

    itn = 0

    # Iterate until the means aren't moving anymore
    while any([threshold < dist for dist in moving_distances]):

        # Step 1 : Assign each observation to a mean
        for obs in observations:
            # Compute the distance to each of the means
            distances = [
                (euclidean_distance(obs, mean), mean.id)
                for mean in means
            ]
            # Assign a the closest mean
            obs.mean = min(distances, key=lambda x: x[0])[1]

        # Step 2 : Update the means
        for idx, mean in enumerate(means):
            # Retrieve all the observations attached to the given mean
            mean_observations = [obs for obs in observations if obs.mean == mean.id]
            # Update the mean as the centroid of the retrived set of observations.
            means[idx] = Mean(centroid(mean_observations), idx)
            # Moving distance
            moving_distances[idx] = euclidean_distance(mean, means[idx])

        itn += 1

        print("Itn {}".format(itn))
        for mean in means:
            print(mean)
        print("\n")

    return means


def init_means(method, observations, k_value, Mean):
    """Initalize means."""
    # If Forgy method
    if method == "forgy":
        # Select a subset of the observations
        subset = random.sample(observations, k_value)
        # Build the means and return them
        return [Mean(obs, idx) for idx, obs in enumerate(subset)]


def euclidean_distance(vect_1, vect_2):
    """Distance between 2 vectors represented by a list-like object."""
    return sum([(val_1 - val_2)**2 for val_1, val_2 in zip(vect_1, vect_2)])**0.5


def centroid(observations):
    """Compute the centroid of a set of observations.
    Args:
        observations (list): list of observations.
    Return:
        centroid (list): the centroid of the observations.
    """
    n_obs = len(observations)
    centroid = [
        round(sum([obs[col] for obs in observations])/n_obs, 8)
        for col in range(len(observations[0]))
    ]
    return centroid


if __name__ == '__main__':
    rows = [
        [random.randint(1, 100) for col_idx in range(4)]
        for row_idx in range(1000)
    ]
    k_value = 3
    threshold = 0.001
    fit(rows, k_value, threshold)
