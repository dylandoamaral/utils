layer=$1

get_versions () {
  echo $(aws lambda list-layer-versions --layer-name "$layer" --output text --query LayerVersions[].Version | tr '[:blank:]' '\n')
}

versions=$(get_versions)
for version in $versions;
do
    echo "deleting arn:aws:lambda:$region:*:layer:$layer:$version"
    aws lambda delete-layer-version --layer-name "$layer" --version-number "$version" > /dev/null
done