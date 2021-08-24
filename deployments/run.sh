set -x
base=$(basename "$1")
cp -r $1 "../$base"
docker-compose build --build-arg root_dir="$1" \
					 --build-arg basename="$base"
rm -r -f "../$base"
docker-compose up