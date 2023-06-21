#! /usr/bin/env python

import torch
import torch.nn as nn
import onnx
from onnxsim import simplify
from argparse import ArgumentParser


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()

    def forward(self, batch, classid, x1y1x2y2, score, pitchyawroll):
        batchno_classid_x1y1x2y2_score_pitchyawroll_cat = torch.cat([batch, classid, x1y1x2y2, score, pitchyawroll], dim=1)
        return batchno_classid_x1y1x2y2_score_pitchyawroll_cat


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        '-o',
        '--opset',
        type=int,
        default=11,
        help='onnx opset'
    )
    args = parser.parse_args()

    model = Model()

    MODEL = f'22_nms_batchno_classid_x1y1x2y2_score_pitchyawroll_cat'

    onnx_file = f"{MODEL}.onnx"
    OPSET=args.opset

    x1 = torch.ones([1, 1], dtype=torch.float32)
    x2 = torch.ones([1, 1], dtype=torch.float32)
    x3 = torch.ones([1, 4], dtype=torch.float32)
    x4 = torch.ones([1, 1], dtype=torch.float32)
    x5 = torch.ones([1, 3], dtype=torch.float32)

    torch.onnx.export(
        model,
        args=(x1,x2,x3,x4,x5),
        f=onnx_file,
        opset_version=OPSET,
        input_names=['cat_batch','cat_classid','cat_x1y1x2y2','cat_score','cat_pitchyawroll'],
        output_names=['batchno_classid_x1y1x2y2_score_pitchyawroll'],
        dynamic_axes={
            'cat_batch': {0: 'N'},
            'cat_classid': {0: 'N'},
            'cat_x1y1x2y2': {0: 'N'},
            'cat_score': {0: 'N'},
            'cat_pitchyawroll': {0: 'N'},
            'batchno_classid_x1y1x2y2_score_pitchyawroll': {0: 'N'},
        }
    )
    model_onnx1 = onnx.load(onnx_file)
    model_onnx1 = onnx.shape_inference.infer_shapes(model_onnx1)
    onnx.save(model_onnx1, onnx_file)

    model_onnx2 = onnx.load(onnx_file)
    model_simp, check = simplify(model_onnx2)
    onnx.save(model_simp, onnx_file)

