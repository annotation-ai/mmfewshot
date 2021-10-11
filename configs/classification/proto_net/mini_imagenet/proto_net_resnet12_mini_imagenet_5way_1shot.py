_base_ = ['proto_net_mini_imagenet_5way_1shot_84x84_aug.py']

model = dict(
    type='ProtoNetClassifier',
    backbone=dict(type='ResNet12'),
    head=dict(type='PrototypeHead'))
