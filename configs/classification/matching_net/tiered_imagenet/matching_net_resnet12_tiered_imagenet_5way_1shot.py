_base_ = ['matching_net_tiered_imagenet_5way_1shot_84x84_aug.py']
model = dict(
    type='MatchingNetClassifier',
    backbone=dict(type='ResNet12'),
    head=dict(type='MatchingHead'))
