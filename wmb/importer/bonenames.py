wmb4_bonenames = {
    0: "HIP",
    1: "spine_1",
    2: "spine_2",
    3: "spine_3",
    4: "neck",
    5: "head",
    6: "shoulder_R",
    7: "upper_arm_R",
    8: "lower_arm_R",
    9: "hand_R",
    10: "shoulder_L",
    11: "upper_arm_L",
    12: "lower_arm_L",
    13: "hand_L",
    
    15: "upper_leg_R",
    16: "lower_leg_R",
    17: "foot_R",
    18: "toe_R",
    19: "upper_leg_L",
    20: "lower_leg_L",
    21: "foot_L",
    22: "toe_L",
    
    1024: "jaw",
    1025: "upper_lip_corner_R",
    1026: "upper_lip_side_R",
    1027: "upper_lip_center",
    1028: "upper_lip_side_L",
    1029: "upper_lip_corner_L",
    1040: "lower_lip_corner_R",
    1033: "lower_lip_side_R",
    1032: "lower_lip_center",
    1031: "lower_lip_side_L",
    1041: "upper_lip_merge_L",
    1042: "lower_lip_merge_L",
    1043: "upper_lip_merge_R",
    1044: "lower_lip_merge_R",
    1030: "lower_lip_corner_L",
    1056: "chin",
    1057: "upper_mouth_crease_L",
    1058: "upper_cheek_1_L",
    1059: "inner_cheek_L",
    1061: "upper_cheek_1_R",
    1060: "upper_mouth_crease_R",
    1062: "inner_cheek_R",
    1063: "upper_cheek_2_L",
    1064: "upper_cheek_2_R",
    1065: "outer_cheek_L",
    1066: "outer_cheek_R",
    1072: "upper_eyelid_1_L",
    1073: "upper_eyelid_2_L",
    1074: "lower_eyelid_2_L",
    1075: "lower_eyelid_1_L",
    1077: "eyebrow_lower_L",
    1078: "eyebrow_L",
    1079: "upper_eyelid_2_R",
    1080: "upper_eyelid_1_R",
    1088: "lower_eyelid_2_R",
    1081: "lower_eyelid_1_R",
    1090: "eyebrow_lower_R",
    1091: "eyebrow_R",
    1092: "eyebrow_crease",
    1104: "eye_L",
    1105: "pupil_L",
    1106: "eye_R",
    1107: "pupil_R",
    1121: "nose",
    1122: "nostril_L",
    1136: "upper_teeth",
    1137: "lower_teeth",
    1138: "nostril_R",
    1139: "tongue",
}
# not gonna duplicate this for both hands
fingers = {
    256: "thumb_1",
    257: "thumb_2",
    258: "thumb_3",
    259: "index_finger_1",
    260: "index_finger_2",
    261: "index_finger_3",
    262: "index_finger_4",
    263: "middle_finger_1",
    264: "middle_finger_2",
    265: "middle_finger_3",
    266: "middle_finger_4",
    267: "ring_finger_1",
    268: "ring_finger_2",
    269: "ring_finger_3",
    270: "ring_finger_4",
    271: "pinkie_1",
    272: "pinkie_2",
    273: "pinkie_3",
    274: "pinkie_4",
}
for ind in fingers.keys():
    name = fingers[ind]
    wmb4_bonenames[ind] = name + "_R"
    wmb4_bonenames[ind + 256] = name + "_L"
