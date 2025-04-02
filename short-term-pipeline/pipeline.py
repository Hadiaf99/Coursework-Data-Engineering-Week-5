"""Script to merge extract, transform and load scripts into a single pipeline"""

from extract import get_plant_data_multiprocessing, save_to_csv
from transform import read_data, save_clean_data_to_csv
from load import get_measurements, ingress_measurements_to_db


def pipeline():
    """Combining all scripts"""
    plant_data = get_plant_data_multiprocessing()
    save_to_csv(plant_data)
    clean_plant_data = read_data("data/plant-measurements.csv")
    save_clean_data_to_csv(clean_plant_data)
    plant_measurements = get_measurements()
    ingress_measurements_to_db(plant_measurements)


if __name__ == "__main__":

    pipeline()
