import argparse
import json
import os
import yaml

def get_args():
  pass

def json_file(file_path):
  pass

def save_json(data, file_path):
  pass

def yaml_file(file_path):
    if not os.path.exists(file_path):
        print("File not found: ", file_path)
        return None

    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except yaml.YAMLError as e:
        print("Error decoding YAML: ", e)
    except Exception as e:
        print("Error: ", e)
    
    return None

def main():
    args = get_args()
    input_file = args.input_file
    output_file = args.output_file

    if input_file.lower().endswith('.json'):
        load_function = json_file
    elif input_file.lower().endswith('.yaml') or input_file.lower().endswith('.yml'):
        load_function = yaml_file
    else:
        print("Unsupported file format. Currently, only .json, .yaml/.yml, and .xml files are supported for reading.")
        return

    data = load_function(input_file)
    if data is None:
        print("Failed to load data.")
        return


    if output_file.lower().endswith('.json'):
        save_json(data, output_file)
    else:
        print("Unsupported file format. Currently, only .yaml/.yml, .json, and .xml files are supported for writing.")
        return

    print("Data successfully saved to ", output_file)

if __name__ == "__main__":
    main()
