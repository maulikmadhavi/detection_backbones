# vitg.vitgyolov8 YOLO 🚀, GPL-3.0 license

from vitg.network.backbone.vitgyolov8.yolo.v8.classify.predict import (
    ClassificationPredictor,
    predict,
)
from vitg.network.backbone.vitgyolov8.yolo.v8.classify.train import (
    ClassificationTrainer,
    train,
)
from vitg.network.backbone.vitgyolov8.yolo.v8.classify.val import (
    ClassificationValidator,
    val,
)

__all__ = [
    "ClassificationPredictor",
    "predict",
    "ClassificationTrainer",
    "train",
    "ClassificationValidator",
    "val",
]
