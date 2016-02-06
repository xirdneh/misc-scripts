metadata-list -Q '{"name": "object"}' | grep '"uuid":' | awk '{print $2}' | sed -e 's/[\",]//g' | while read x; do
    metadata-delete $x
    echo $x
done
