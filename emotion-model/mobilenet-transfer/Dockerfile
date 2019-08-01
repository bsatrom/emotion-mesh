# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# #==========================================================================

FROM tensorflow/tensorflow:1.11.0-rc2-devel

# Get the tensorflow models research directory, and move it into tensorflow
# source folder to match recommendation of installation
RUN git clone https://github.com/tensorflow/models.git && \
    mv models /tensorflow/models

# Install wget (to make life easier below) and editors (to allow people to edit
# the files inside the container)
RUN apt-get update && \
    apt-get install -y wget vim emacs nano

ARG work_dir=/tensorflow/models/research/slim
# Get classification transfer learning scripts.
ARG scripts_link="http://storage.googleapis.com/cloud-iot-edge-pretrained-models/docker/classify_scripts.tgz"
RUN cd ${work_dir} && \
    wget -O classify_scripts.tgz ${scripts_link} && \
    tar zxvf classify_scripts.tgz

WORKDIR ${work_dir}
