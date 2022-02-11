jq -s '.' ./primary_jsons/*.json > output.json

jq 'sort_by(.date|split("-")|map(tonumber))' output.json > ordered_output.json
jq 'sort_by(.year|map(tonumber))' ordered_output.json > primaries.json

rm output.json
rm ordered_output.json

jq -s '.' ./secondary_jsons/*.json > output.json

jq 'sort_by(.date|split("-")|map(tonumber))' output.json > ordered_output.json
jq 'sort_by(.year|map(tonumber))' ordered_output.json > secondaries.json

rm output.json
rm ordered_output.json

# diff -y output.json ordered_output.json