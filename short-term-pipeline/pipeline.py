from extract import get_plant_data_multiprocessing, save_to_csv
from transform import save_clean_data_to_csv, read_data
from load import get_measurements, ingress_measurements_to_db, DATA_PATH
from dotenv import load_dotenv


def pipeline():
    load_dotenv()
    plant_data = get_plant_data_multiprocessing()
    save_to_csv(plant_data, "data/plant-measurements.csv")
    final_data = read_data("data/plant-measurements.csv")
    save_clean_data_to_csv(final_data)
    plant_measurements = get_measurements()
    ingress_measurements_to_db(plant_measurements)


if __name__ == "__main__":

    pipeline()
