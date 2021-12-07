jq -cr 'keys[] as $k | "\($k)\n\(.[$k])"' secondary_data_json.json | while read -r key; do
  fname=$(jq --raw-output ".[$key].bibtex" secondary_data_json.json)
  read -r item
  printf '%s\n' "$item" > "./jsons/$fname.json"
done