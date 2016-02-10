#metadata-list -V -Q '{"name": "designsafe metadata"}' | grep '"uuid":' | awk '{print $2}' | sed -e 's/[\",]//g' | while read x; do
metadata-list -V -Q '{"name": "designsafe metadata"}' | while read x; do metadata-delete $x; done;
