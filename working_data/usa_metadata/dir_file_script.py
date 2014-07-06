import json
import os
import errno
import shutil

source_path = "/Users/mikecap/Sites/food-fiddle/working_data/usa_metadata/"
#"/food-fiddle/clean_data/general/corpora/"

destination_path = "/Users/mikecap/Sites/food-fiddle/source_data/state/"
#"/food-fiddle/source_data/state/"

json_file = "20140704221735_united_states_metadata.json"
readme_file = "README.md"
source_path_file = source_path + readme_file

# Read states_metadata.json
json_data = open(source_path + json_file)

state_dict_list = json.load(json_data)

for each_dictionary in state_dict_list["States metadata"]:
    if "USPS" in each_dictionary.keys():
        postal_code = each_dictionary["USPS"]
        state_status = each_dictionary["Status"]

        if (postal_code) and ((state_status == "State") or (state_status == "State (Commonwealth)") or (state_status == "Federal district")):
            # Create folder with name USPS
            destination_path_new = destination_path + postal_code

            try:
                os.makedirs(destination_path_new)
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise

            # Copy README file into folder
            try:
                shutil.copyfile(source_path_file, destination_path_new + "/" + readme_file)
            except IOError as exception:
                raise

json_data.close()
