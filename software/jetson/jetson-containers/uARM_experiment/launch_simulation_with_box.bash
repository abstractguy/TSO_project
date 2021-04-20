#!/bin/bash
export GAZEBO_MODEL_PATH=models/
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:build/
gazebo world/uarm_world_with_box.world
source ~/.bashrc
