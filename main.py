import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', help='Ruta de la carpeta con múltiples archivos')
parser.add_argument('--bucket', help='Nombre del bucket de S3', required=True)
args = parser.parse_args()



for filename in os.listdir(args.input_dir):
    file_path = os.path.join(args.input_dir, filename)
    print(file_path)

