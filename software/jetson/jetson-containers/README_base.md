# Build instructions

```bash
sudo make image
sudo make push
```

# Architecture Details

Use cases addressed by this image:
1) Be able to run gstreamer samples (during a docker run)
2) Be able to run tensorrt samples (during a docker run)
3) Be able to compile CUDA code (Both for docker run and docker build)

The current build system is a 3 step process:
- Build a full blown CUDA "devel" container
- Copy the cuda headers and stubs on the host and clean them up (removing sobol_direction_vectors.h which weighs 60M)
- Build the base container with the CUDA headers and stubs

This three step process is done in this way to be able to satisfy #3.
In the future we should probably just install the CUDA packages in such a way that we mirror "cuda-base" on x86.
This would allow us to reduce the build to a single Dockerfile while incurring a small size increase (~100M).

# Adding container path
Update the container paths $L4T_CUDA_REGISTRY and $L4T_BASE_REGISTRY as applicable

# Adding a new release

Don't forget to do the following:
- Bump the RELEASE variable
- Add the CUDA packages in a directory pointed to by the $RELEASE variable

# Size Estimates

* ~505MB If l4t-base is composed of only cuda-base packages
    * You can't do anything related to NVIDIA at docker build time (e.g: Compilation)
    * You also can't do anything related to NVIDIA using qemu user on an x86 machine
* ~1.5G if l4t-base is composed of only cuda-runtime packages
    * You can't do anything related to NVIDIA at docker build time (e.g: Compilation)
    * You also can't do anything related to NVIDIA using qemu user on an x86 machine
* ~2.5G if l4t-base is composed of the cuda-devel packages
    * You can build CUDA code with docker build and on an x86 machine
* ~600MB if you use the current hybrid technique
    * We build a cuda-devel container and copy the stubs + headers


# libpod Installation Instructions


#### [Ubuntu](https://www.ubuntu.com)

```bash
sudo apt-get update -qq
sudo apt-get install -qq -y software-properties-common uidmap
sudo add-apt-repository -y ppa:projectatomic/ppa
sudo apt-get update -qq
sudo apt-get -qq -y install podman
```

