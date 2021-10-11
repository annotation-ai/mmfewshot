_base_ = [
    '../../../_base_/datasets/finetune_based/few_shot_voc.py',
    '../../../_base_/schedules/schedule.py',
    '../../tfa_faster_rcnn_r101_fpn.py', '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotVOCDataset
# FewShotVOCDefaultDataset predefine ann_cfg for model reproducibility.
data = dict(
    train=dict(
        type='FewShotVOCDefaultDataset',
        ann_cfg=[dict(method='TFA', setting='SPLIT1_1SHOT')],
        num_novel_shots=1,
        num_base_shots=1,
        classes='ALL_CLASSES_SPLIT1'),
    val=dict(classes='ALL_CLASSES_SPLIT1'),
    test=dict(classes='ALL_CLASSES_SPLIT1'))
evaluation = dict(
    interval=4000,
    class_splits=['BASE_CLASSES_SPLIT1', 'NOVEL_CLASSES_SPLIT1'])
checkpoint_config = dict(interval=4000)
optimizer = dict(lr=0.001)
lr_config = dict(
    warmup=None, step=[
        3000,
    ])
runner = dict(max_iters=4000)
# load_from = 'path of base training model'
load_from = \
    'work_dirs/' \
    'tfa_faster_rcnn_r101_fpn_voc_split1_base_training/' \
    'model_reset_randinit.pth'
