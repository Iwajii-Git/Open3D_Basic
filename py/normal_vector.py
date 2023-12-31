import open3d as o3d
import numpy as np

#点群の読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")

#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)

#法線推定
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

#点群の表示
o3d.visualization.draw_geometries([pcd], point_show_normal=True)    
