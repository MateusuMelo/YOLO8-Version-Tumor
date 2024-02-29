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
<div align='center'>
      
|precision_mean|box_loss_mean|cls_loss_mean|
|------------|-------------|-------------|
|91.59%|0.69|0.91|

![alt text](https://raw.githubusercontent.com/MateusuMelo/YOLO8-Version-Tumor/dd487df16de467a0a15947e98a8798a5990bdb8f/results_img/Yolov8-N/results.png)

</div>

<summary>YOLOv8-s</summary>
<div align='center'>
      
|precision_mean|box_loss_mean|cls_loss_mean|
|------------|-------------|-------------|
|84.63%|0.85|1.11|

![alt text](https://raw.githubusercontent.com/MateusuMelo/YOLO8-Version-Tumor/dd487df16de467a0a15947e98a8798a5990bdb8f/results_img/Yolov8-S/results.png)

</div>

<summary>YOLOv8-m</summary>
<div align='center'>
      
|precision_mean|box_loss_mean|cls_loss_mean|
|------------|-------------|-------------|
|91.31%|0.71|0.74|

![alt text](https://raw.githubusercontent.com/MateusuMelo/YOLO8-Version-Tumor/dd487df16de467a0a15947e98a8798a5990bdb8f/results_img/Yolov8-M/results.png)

</div>

<summary>YOLOv8-l</summary>
<div align='center'>
      
|precision_mean|box_loss_mean|cls_loss_mean|
|------------|-------------|-------------|
|91.58%|0.73|0.99|

![alt text](https://raw.githubusercontent.com/MateusuMelo/YOLO8-Version-Tumor/dd487df16de467a0a15947e98a8798a5990bdb8f/results_img/Yolov8-L/results.png)

</div>

<summary>YOLOv8-x</summary>
<div align='center'>
      
|precision_mean|box_loss_mean|cls_loss_mean|
|------------|-------------|-------------|
|93.87%|0.69|0.66|

![alt text](https://raw.githubusercontent.com/MateusuMelo/YOLO8-Version-Tumor/dd487df16de467a0a15947e98a8798a5990bdb8f/results_img/Yolov8-X/results.png)

</div>
