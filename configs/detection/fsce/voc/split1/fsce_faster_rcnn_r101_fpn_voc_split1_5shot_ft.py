_base_ = [
    '../../../_base_/datasets/finetune_based/few_shot_voc.py',
    '../../../_base_/schedules/schedule.py',
    '../../fsce_faster_rcnn_r101_fpn.py', '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotVOCDataset
# FewShotVOCDefaultDataset predefine ann_cfg for model reproducibility.
data = dict(
    train=dict(
        type='FewShotVOCDefaultDataset',
        ann_cfg=[dict(method='FSCE', setting='SPLIT1_5SHOT')],
        num_novel_shots=5,
        num_base_shots=5,
        classes='ALL_CLASSES_SPLIT1'),
    val=dict(classes='ALL_CLASSES_SPLIT1'),
    test=dict(classes='ALL_CLASSES_SPLIT1'))
evaluation = dict(
    interval=4500,
    class_splits=['BASE_CLASSES_SPLIT1', 'NOVEL_CLASSES_SPLIT1'])
checkpoint_config = dict(interval=4500)
optimizer = dict(lr=0.001)
lr_config = dict(warmup_iters=200, gamma=0.5, step=[5000, 7000])
runner = dict(max_iters=9000)
# load_from = 'path of base training model'
load_from = \
    'work_dirs/' \
    'fsce_faster_rcnn_r101_fpn_voc_split1_base_training/' \
    'model_reset_randinit.pth'
