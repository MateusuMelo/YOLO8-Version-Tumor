## Treinamento e Inferência das sub-versões do YoloV8-detection em um dataset customizado de imagens medicas de tumores cerebrais

## 1.Dataset
O dataset usado : [Roboflow - BrainTumor](https://universe.roboflow.com/csilab/csilab-braintumor-detection).<br>
A separação de dados :
|Train|Test|Valid|
|-----|----|-----|
|211|60|30|
|70%|20%|10%|


## 2.Modelos e parametros

<summary>modelos usados (retirado da documentacao do Yolov8)</summary>
<div align = 'center'>
      <table>
    <thead>
    <tr>
    <th>Modelo</th>
    <th>tamanho<br><sup>(pixéis)</sup></th>
    <th>mAPval<sup><br>50-95</sup></th>
    <th>Velocidade<br><sup>CPU ONNX<br> (ms)</sup></th>
    <th>Velocidade<br> A100<sup> TensorRT<br>(ms)</sup></th>
    <th>params<br><sup>(M)</sup></th>
    <th>FLOPs<br><sup>(B)</sup></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><a href="https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt">YOLOv8n</a></td>
    <td>640</td>
    <td>37.3</td>
    <td>80.4</td>
    <td>0.99</td>
    <td>3.2</td>
    <td>8.7</td>
    </tr>
    <tr>
    <td><a href="https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8s.pt">YOLOv8s</a></td>
    <td>640</td>
    <td>44.9</td>
    <td>128.4</td>
    <td>1.20</td>
    <td>11.2</td>
    <td>28.6</td>
    </tr>
    <tr>
    <td><a href="https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m.pt">YOLOv8m</a></td>
    <td>640</td>
    <td>50.2</td>
    <td>234.7</td>
    <td>1.83</td>
    <td>25.9</td>
    <td>78.9</td>
    </tr>
    <tr>
    <td><a href="https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8l.pt">YOLOv8l</a></td>
    <td>640</td>
    <td>52.9</td>
    <td>375.2</td>
    <td>2.39</td>
    <td>43.7</td>
    <td>165.2</td>
    </tr>
    <tr>
    <td><a href="https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8x.pt">YOLOv8x</a></td>
    <td>640</td>
    <td>53.9</td>
    <td>479.1</td>
    <td>3.53</td>
    <td>68.2</td>
    <td>257.8</td>
    </tr>
    </tbody>
    </table>
</div>


Todos os treinamentos foram realizados na NVIDIA A100.
<div align='center'>

| Models | BatchSize | epochs | Resolution |
|-|-|:-:|:-:|
| YOLOv8-n  |32| 1000 | 640x640 |
| YOLOv8-s  | 32 | 1000 | 640x640 |
| YOLOv8-m  | 32 | 1000 | 640x640 |
| YOLOv8-l  | 32 | 1000 | 640x640 |
| YOLOv8-X  | 32 | 1000 | 640x640 |
</div>


## 4.Resultados

<summary>YOLOv8-n</summary>

|precision_mean|box_loss_mean|cls_loss_mean|
|------------|-------------|-------------|
|78.36%|60.79|204.12|

<details open>
|      
      
</details>
```
git clone https://github.com/Li-Hongda/TensorRT_Inference_Demo.git
```
2. Install the dependencies.
### TensorRT
Following [NVIDIA offical docs](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing) to install TensorRT.

### yaml-cpp
```
git clone https://github.com/jbeder/yaml-cpp
mkdir build && cd build
cmake ..
make -j20
cmake -DYAML_BUILD_SHARED_LIBS=on ..
make -j20
cd ..
```


3. Change the path [here](https://github.com/Li-Hongda/TensorRT_Inference_Demo/blob/main/object_detection/CMakeLists.txt#L19) to your TensorRT path, and [here](https://github.com/Li-Hongda/TensorRT_Inference_Demo/blob/main/object_detection/CMakeLists.txt#L11) to your CUDA path. Then,
```
cd TensorRT_Inference_Demo/object_detection
mkdir build && cd build
cmake ..
make -j$(nproc)
```
4. Get the ONNX model from the official repository and put them in `weights/MODEL_NAME`. Then modify the configuration file in `configs`.Take yolov5 as an example:
```
python export.py --weights=yolov5s.pt  --dynamic --simplify --include=onnx --opset 11
```
5. The executable file will be generated in `bin` in the repo directory if compile successfully.Then enjoy yourself with command like this:
```
cd bin
./object_detection yolov5 /path/to/input/dir 
```

> Notes:
> 1. The output of the model is required for post-processing is num_bboxes (imageHeight x imageWidth) x num_pred(num_cls + coordinates + confidence),while the output of YOLOv8 is num_pred x num_bboxes,which means the predicted values of the same box are not contiguous in memory.For convenience, the corresponding dimensions of the original pytorch output need to be transposed when exporting to ONNX model.
> 2. The dynamic shape engine is convenient but sacrifices some inference speed compared with the static model of the same batchsize.Therefore, if you want to pursue faster inference speed, it is better to export the ONNX model of fixed batchsize, such as batchsize 32.



