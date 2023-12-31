import open3d as o3d
import numpy as np

#点群読み込み
pcd = o3d.io.read_point_cloud("cow_data.ply")

#ダウンサンプリング
pcd = pcd.voxel_down_sample(voxel_size=0.01)

#法線推定
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

#面に対する法線方向の一貫性を保つ
pcd.orient_normals_consistent_tangent_plane(100)
       
#各点の最近傍点までの距離を算出している
distances = pcd.compute_nearest_neighbor_distance()

#最近傍点までの距離の平均を出している
avg_dist = np.mean(distances)

#最近傍点までの平均の値を二倍する
radius = 2*avg_dist   

#半径の引数radii作成
radii = [radius, radius * 2]

#メッシュの作成
recMeshBPA = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, o3d.utility.DoubleVector(radii))
       
#作成したメッシュの表示
o3d.visualization.draw_geometries([recMeshBPA])
