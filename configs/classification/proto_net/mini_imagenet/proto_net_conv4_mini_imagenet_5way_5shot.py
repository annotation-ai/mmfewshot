_base_ = ['proto_net_mini_imagenet_5way_5shot_84x84_aug.py']
model = dict(
    type='ProtoNetClassifier',
    backbone=dict(type='Conv4'),
    head=dict(type='PrototypeHead'))
