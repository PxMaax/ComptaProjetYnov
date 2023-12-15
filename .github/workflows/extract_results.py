import json

def extract_results(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    results = []
    for file_result in data['files']:
        file_name = file_result['path']
        file_score = file_result['statistics']['global_note']
        last_developer = file_result['violations'][0]['author']  # Adapt as needed

        result_info = f"{file_name}, Note: {file_score}/10, Last Developer: {last_developer}"
        results.append(result_info)

    with open('lint_summary.txt', 'w') as output_file:
        output_file.write('\n'.join(results))

if __name__ == "__main__":
    extract_results('pylint_results.json')
