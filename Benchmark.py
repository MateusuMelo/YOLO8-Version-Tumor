from ultralytics import YOLO
import pandas as pd
import os


def getBenchMark(model_path, data_path):
    model = YOLO(model_path)
    results = model(data_path)

    data = pd.DataFrame()
    for result in results:
        df_dictionary = pd.DataFrame([result.speed])
        data = pd.concat([data, df_dictionary], ignore_index=True)

    data_final = {'preprocess_min': data['preprocess'].min(), 'preprocess_max': data['preprocess'].max(),
                  'preprocess_mean': data['preprocess'].mean(),
                  'inference_min': data['inference'].min(), 'inference_max': data['inference'].max(),
                  'inference_mean': data['inference'].mean(),
                  'postprocess_min': data['postprocess'].min(), 'postprocess_max': data['postprocess'].max(),
                  'postprocess_mean': data['postprocess'].mean(), }
    data_final = pd.DataFrame([data_final])

    model_name = model_path.split('/')[-3]
    directory = f"runs/benchmark/{model_name}"

    if not os.path.exists(directory):
        os.makedirs(directory)

    return data_final.to_csv(f"{directory}/results.csv", index=False)


def benchmarkModelsInFolder(models_folder, data_path):
    models = os.listdir(models_folder)
    for model in models:
        print(f"Model : {model}")
        getBenchMark(f"{models_folder}/{model}/weights/best.pt", data_path)
    return None


benchmarkModelsInFolder(".models", ".dataset/valid/images/")
