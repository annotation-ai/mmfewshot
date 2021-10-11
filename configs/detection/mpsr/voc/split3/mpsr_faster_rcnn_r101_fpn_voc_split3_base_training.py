_base_ = [
    '../../../_base_/datasets/two_branch/base_voc.py',
    '../../../_base_/schedules/schedule.py',
    '../../mpsr_faster_rcnn_r101_fpn.py', '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotVOCDataset
data = dict(
    train=dict(dataset=dict(classes='BASE_CLASSES_SPLIT3')),
    val=dict(classes='BASE_CLASSES_SPLIT3'),
    test=dict(classes='BASE_CLASSES_SPLIT3'))
evaluation = dict(interval=9000, class_splits=['BASE_CLASSES_SPLIT3'])
checkpoint_config = dict(interval=3000)
optimizer = dict(
    lr=0.005,
    paramwise_cfg=dict(
        custom_keys={'.bias': dict(lr_mult=2.0, decay_mult=0.0)}))
lr_config = dict(warmup_iters=500, step=[24000, 32000])
runner = dict(max_iters=36000)
model = dict(roi_head=dict(bbox_head=dict(num_classes=15)))
