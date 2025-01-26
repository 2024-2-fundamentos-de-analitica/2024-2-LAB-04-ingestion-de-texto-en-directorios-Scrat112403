# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import zipfile
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    zip_path = "files/input.zip"
    base_path = "files/input"
    output_dir = "files/output"     

    with zipfile.ZipFile(zip_path, "r") as zip:
        zip.extractall("files")

    def read(base_path, folder, sentiment):
        folder_path = os.path.join(base_path, folder, sentiment)
        return [
            {"phrase": open(os.path.join(folder_path, file), "r").read(), "target": sentiment}
            for file in os.listdir(folder_path)
        ]

    def process_data(base_path, data_type):
        sentiments = ["negative", "positive", "neutral"]
        data = []
        for sentiment in sentiments:
            data.extend(read(base_path, data_type, sentiment))
        return data


    train_data = process_data(base_path, "train")
    test_data = process_data(base_path, "test")
    pd.DataFrame(train_data).to_csv((os.path.join(output_dir, "train_dataset.csv")), index=False)
    pd.DataFrame(test_data).to_csv((os.path.join(output_dir, "test_dataset.csv")), index=False)
    os.makedirs(output_dir, exist_ok=True)
        

pregunta_01
