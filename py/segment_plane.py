import open3d as o3d
import numpy as np

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")
#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)
#点群の表示
o3d.visualization.draw_geometries([pcd])

#平面推定
plane_model, inliers = pcd.segment_plane(distance_threshold=0.02, ransac_n=4, num_iterations=10000)

#平面の式の係数
[a, b, c, d] = plane_model
#推定した平面の式の表示
print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

#平面上の点と認識された点を選択
plane_cloud = pcd.select_by_index(inliers)
#平面上の点を赤色に着色
plane_cloud.paint_uniform_color([1.0, 0, 0])

#平面上の点と認識されなかった点を選択
outlier_cloud = pcd.select_by_index(inliers, invert=True)

#点群の表示
o3d.visualization.draw_geometries([plane_cloud, outlier_cloud])