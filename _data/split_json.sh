jq -cr 'keys[] as $k | "\($k)\n\(.[$k])"' output.json | while read -r key; do
  fname=$(jq --raw-output ".[$key].bibtex" output.json)
  read -r item
  printf '%s\n' "$item" > "./primary_jsons/$fname.json"
done