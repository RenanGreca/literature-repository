jq -s '.' ./jsons/*.json > output.json

jq 'sort_by(.date|split("-")|map(tonumber))' output.json > ordered_output.json

# diff -y output.json ordered_output.json