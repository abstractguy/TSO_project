REBUILD=0
while getopts 'r' opt
do
    case $opt in
        r) REBUILD=1 ;;
        *) echo 'Error in command line parsing' >&2
           exit 1
        esac
done
shift "$(( OPTIND - 1 ))"

#CHOICE=$(echo "${1:-n}" | tr '[:upper:]' '[:lower:]')

if [ $# -eq 0 ]
then
    echo "Specify the ROS distribution to use (example: kinetic, melodic)..."
fi

BASE_IMAGE=ros
BASE_TAG=$1

docker pull ${BASE_IMAGE}:${BASE_TAG}

#NAME=ros_ws
NAME=catkin_ws

#UID="$(id -u $USER)"
#GID="$(id -g $USER)"

UID=1000
GID=1000

if [ "$REBUILD" -eq 1 ]
then
    docker build --no-cache \
                 --build-arg BASE_IMAGE=${BASE_IMAGE} \
                 --build-arg BASE_TAG=${BASE_TAG} \
                 --build-arg UID=${UID} \
                 --build-arg GID=${GID} \
                 -f Dockerfile \
                 -t ${NAME}:${BASE_TAG} .
else
    docker build --build-arg BASE_IMAGE=${BASE_IMAGE} \
                 --build-arg BASE_TAG=${BASE_TAG} \
                 --build-arg UID=${UID} \
                 --build-arg GID=${GID} \
                 -f Dockerfile \
                 -t ${NAME}:${BASE_TAG} .
fi
